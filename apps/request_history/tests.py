from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve
from .models import MyRequest
from datetime import datetime


class Request_test(TestCase):

    def test_request_view(self):
        """ Test the request view """

        found = resolve('/request_history')
        self.assertEqual(found.func.__name__, 'RequestHistory')

        self.client = Client()
        url = reverse("request_history")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_the_model_Info(self):
        """Test the model Request_model"""

        instance = MyRequest()
        instance.request_method = 'POST'
        instance.request_link = 'http://127.0.0.1:8000/'
        instance.request_time = datetime.now()
        instance.save()

        saved_items = MyRequest.objects.all()
        first_query = saved_items[0]
        self.assertEqual(first_query.request_method, "POST")
        self.assertEqual(first_query.request_link, "http://127.0.0.1:8000/")

    def test_request_middleware_stors_requests(self):
        """ Test for middleware grab request and save in db"""

        for c in range(4):
            url = reverse("home")
            response = self.client.post(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MyRequest.objects.all().count(), 5)

    def test_request_to_store_only_10_request_to_database(self):
        """ Test for middleware grab only 10 request and save in db"""
        for c in range(15):
            url = reverse("home")
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(MyRequest.objects.all().count(), 10)

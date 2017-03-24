from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve
from .models import Request_model
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
        self.assertIn(b'POST', response.content)
        self.assertIn(b'http://127.0.0.1:8000/', response.content)

    def test_the_model_Info(self):
        """Test the model Request_model"""

        instance = Request_model()
        instance.method = 'POST'
        instance.link = 'http://127.0.0.1:8000/'
        instance.date = datetime.now()
        instance.save()

        saved_items = Request_model.objects.all()
        first_query = saved_items[0]
        self.assertEqual(first_query.method, "POST")
        self.assertEqual(first_query.link, "http://127.0.0.1:8000/")

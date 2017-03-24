from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve


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
        self.assertIn(b'22:51 23.03.2017', response.content)

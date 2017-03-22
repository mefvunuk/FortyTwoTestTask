from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve
# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)

    def test_the_view(self):
        """Test for the view returning hard-coded data for the template"""

        found = resolve('/')
        self.assertEqual(found.func.__name__, 'Home_view')

        self.client = Client()
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Oleg', response.content)
        self.assertIn(b'Vunuk', response.content)
        self.assertIn(b'mefvunuk@gmail.com', response.content)

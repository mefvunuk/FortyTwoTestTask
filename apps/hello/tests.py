from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse, resolve
from .models import Info
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

    def test_the_model_Info(self):
        """Test the model Info"""

        instance = Info()
        instance.name = 'Oleg'
        instance.surname = 'Vunuk'
        instance.date = '1989-09-02'
        instance.bio = 'live in Lviv'
        instance.email = 'mefvunuk@gmail.com'
        instance.jabber = 'mefvunuk@42cc.co'
        instance.contacts = 'None'
        instance.skype = 'None'
        instance.save()

        saved_items = Info.objects.all()
        first_query = saved_items[1]
        self.assertEqual(first_query.name, "Oleg")
        self.assertEqual(first_query.surname, "Vunuk")
        self.assertEqual(first_query.bio, "live in Lviv")
        self.assertEqual(first_query.email, "mefvunuk@gmail.com")
        self.assertEqual(first_query.jabber, "mefvunuk@42cc.co")

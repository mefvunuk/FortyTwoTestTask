from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date = models.DateField()
    bio = models.TextField(blank=True)
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=200, blank=True)
    contacts = models.TextField(blank=True)

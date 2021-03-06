from django.test import TestCase, Client
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth


class TestViews(TestCase):
    def test_home_page_loads(self):
        home = self.client.get("/")
        self.assertEqual(home.status_code, 200)
        self.assertTemplateUsed(home, "index.html")

   
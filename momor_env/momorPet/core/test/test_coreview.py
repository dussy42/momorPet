from django.test import TestCase, Client
from django.urls import reverse

import json


from core.views import frontpage, about


class Test_core_views(TestCase):

    def setUp(self):
        self.client = Client()
        self.frontpage_url = reverse('frontpage')
        self.about_url = reverse('about')

    def test_frontpage_view(self):
        response = self.client.get(self.frontpage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/frontpage.html')

    def test_about_view(self):
        response = self.client.get(self.about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/about.html')

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import frontpage, about


class Test_core_urls(SimpleTestCase):

    def test_frontpage_url_resolves(self):
        url = reverse('frontpage')
        self.assertEquals(resolve(url).func, frontpage)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

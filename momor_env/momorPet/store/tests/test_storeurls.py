from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import add_to_cart, success, change_quantity, remove_from_cart, cart_view, checkout, search, category_detail, product_detail


class Test_store_urls(SimpleTestCase):

    def test_add_to_cart_url_resolves(self):
        url = reverse('add_to_cart')
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_success_url_resolves(self):
        url = reverse('success')
        self.assertEquals(resolve(url).func, success)

    def test_change_quantity_url_resolves(self):
        url = reverse('change_quantity')
        self.assertEquals(resolve(url).func, change_quantity)

    def test_remove_from_cart_url_resolves(self):
        url = reverse('remove_from_cart')
        self.assertEquals(resolve(url).func, remove_from_cart)

    def test_cart_view_url_resolves(self):
        url = reverse('cart_view')
        self.assertEquals(resolve(url).func, cart_view)

    def test_checkout_url_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_search_url_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_category_detail_url_resolves(self):
        url = reverse('category_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, category_detail)

    def test_product_detail_url_resolves(self):
        url = reverse('product_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, product_detail)

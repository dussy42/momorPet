from django.test import TestCase, Client
from django.urls import reverse
from store.models import OrderItem, Order, Product, Category
import json
from django.utils.text import slugify


class Test_store_views(TestCase):

    def setUp(self):
        self.client = Client()
        self.change_quantity_url = reverse('change_quantity')
        self.search_url = reverse('search')
        self.success_url = reverse('success')
        self.add_to_cart_url = reverse('add_to_cart')
        self.remove_from_cart_url = reverse('remove_from_cart')
        self.cart_view_url = reverse('cart_view')
        self.category = Category.objects.create(name='category_detail',)
        self.product = Product.objects.create(name='product_detail',)

    def test_change_quantity_GET(self):

        response = self.client.get(self.change_quantity_url)

        self.assertEquals(response.status_code, 302)

    def test_search_GET(self):
        response = self.client.get(self.search_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/search.html')

    def test_success(self):
        response = self.client.get(self.success_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/success.html')

    def test_add_to_cart(self):
        response = self.client.get(self.add_to_cart_url)

        self.assertEquals(response.status_code, 302)

    def test_remove_from_cart(self):
        response = self.client.get(self.remove_from_cart_url)

        self.assertEquals(response.status_code, 302)

    def test_cart_view(self):
        response = self.client.get(self.cart_view_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart_view.html')

    def test_category_detail(self):
        slug = slugify(self.category.category_detail)
        url = reverse('category_detail', kwargs={'slug': slug})
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/category_detail.html')
        self.assertContains(response, self.category.category_detail)

    def test_product_detail(self):
        slug = slugify(self.product.product_detail)
        url = reverse('product_detail', kwargs={'slug': slug})
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/product_detail.html')
        self.assertContains(response, self.product.product_detail)

    def test_checkout_with_valid_data(self):
        data = {
            'first_name': 'Momoh',
            'last_name': 'sam',
            'address': 'ireland',
            'zipcode': '98765',
            'city': 'Dublin',
        }
        response = self.client.post(reverse('checkout'), data=data)

        self.assertEquals(response.status_code, 200)
        self.assertTrue(Order.objects.exists())
        self.assertTrue(OrderItem.objects.exists())

    def test_checkout_with_invalid_data(self):
        data = {
            'first_name': '',
            'last_name': '',
            'address': '',
            'zipcode': '',
            'city': '',
        }
        response = self.client.post(reverse('checkout'), data=data)

        self.assertEquals(response.status_code, 404)
        self.assertFormError(response, 'form', 'first_name',
                             'This field is required.')
        self.assertFormError(response, 'form', 'last_name',
                             'This field is required.')
        self.assertFormError(response, 'form', 'address',
                             'This field is required.')
        self.assertFormError(response, 'form', 'zipcode',
                             'This field is required.')
        self.assertFormError(response, 'form', 'city',
                             'This field is required.')

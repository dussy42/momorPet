from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Category, Product
from userprofile.models import Userprofile


class Test_user_profile_views(TestCase):
    def setUp(self):
        self.client = Client()
        self.my_store_url = reverse('my_store')
        self.myaccount_url = reverse('myaccount')
        self.my_store_order_detail_url = reverse('my_store_order_detail')
        self.client.login(username='momoh', password='testpassword')
        self.user = User.objects.create_user(
            username='momoh',
            password='testpassword'
        )
        self.product = Product.objects.create(
            title='Test Product',
            description='This is a test product.',

        )

    def test_signup_view(self):

        new_user_data = {
            'username': 'newuser',

            'password2': 'newpassword123',

        }

        signup_url = reverse('signup')

        response = self.client.post(signup_url, new_user_data)

        self.assertEqual(response.status_code, 302)

        user_exists = Userprofile.objects.filter(username='newuser').exists()

        self.assertTrue(user_exists)

    def test_delete_product_view(self):

        delete_product_url = reverse('delete_product', kwargs={
                                     'pk': self.product.pk})

        response = self.client.post(delete_product_url)

        self.assertEqual(response.status_code, 302)

        product_exists = Product.objects.filter(pk=self.product.pk).exists()

        self.assertFalse(product_exists)

    def test_edit_product_view(self):

        updated_product_data = {
            'title': 'Updated Test Product',
            'description': 'This is an updated test product.',

        }

        edit_product_url = reverse('edit_product', kwargs={
                                   'pk': self.product.pk})

        response = self.client.post(edit_product_url, updated_product_data)

        self.assertEqual(response.status_code, 302)

        updated_product = Product.objects.get(pk=self.product.pk)

        self.assertEqual(updated_product.title, 'Updated Test Product')
        self.assertEqual(updated_product.description,
                         'This is an updated test product.')

    def test_add_product_view(self):

        self.client.login(username='momoh', password='testpassword')

        product_data = {
            'name': 'Test Product',
            'description': 'This is a test product.',

        }

        add_product_url = reverse('add_product')

        response = self.client.post(add_product_url, product_data)

        self.assertEqual(response.status_code, 302)

    def test_my_store(self):
        response = self.client.get(self.my_store_url)

        self.assertTemplateUsed(response, 'userprofile/my_store.html')

        self.assertEqual(response.status_code, 200)

    def test_my_store_order_detail(self):
        response = self.client.get(self.my_store_order_detail_url)

        self.assertTemplateUsed(
            response, 'userprofile/my_store_order_detail.html')

        self.assertEqual(response.status_code, 200)

    def test_myaccount(self):
        response = self.client.get(self.myaccount_url)

        self.assertTemplateUsed(response, 'userprofile/myaccount.html')

        self.assertEqual(response.status_code, 200)

    def test_vendor_detail_view_with_valid_id(self):

        url = reverse('vendor_detail', kwargs={'vendor_id': self.vendor.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_vendor_detail_view_with_invalid_id(self):

        invalid_vendor_id = 99999

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

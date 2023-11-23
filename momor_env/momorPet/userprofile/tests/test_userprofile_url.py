from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import frontpage, about
# Import the User model or your custom User model
from django.contrib.auth.models import User
from userprofile.models import Userprofile


class Test_userprofile_urls(SimpleTestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='momoh',
            password='testpassword'
        )

        self.user_profile = Userprofile.objects.create(
            user=self.user,
            vendor_url='https://example.com/vendor'
        )

    def test_vendor_url(self):

        user_profile = Userprofile.objects.get(user=self.user)

        vendor_url = user_profile.vendor_url

        self.assertEqual(vendor_url, 'https://example.com/vendor')

    def test_signup_url(self):

        url = reverse('signup')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_login_url(self):

        url = reverse('login')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_myaccount_url(self):

        url = reverse('myaccount')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_my_store_url(self):

        url = reverse('my_store')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_my_store_order_detail(self):

        url = reverse('my_store_order_detail')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_add_product(self):

        url = reverse('add_product')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_edit_product(self):

        url = reverse('edit_product')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):

        url = reverse('delete_product')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_vendor_detail(self):

        url = reverse('vendor_detail')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.urls import reverse
from .models import Vendor  # Import your Vendor model


class Test_user_profile_views(TestCase):
    def setUp(self):

        self.vendor = Vendor.objects.create(
            name='vendor_detail',

        )

    def test_vendor_detail_view_with_valid_id(self):

        # Replace 'vendor_id' with your actual URL parameter
        url = reverse('vendor_detail', kwargs={'vendor_id': self.vendor.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_vendor_detail_view_with_invalid_id(self):

        invalid_vendor_id = 99999

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

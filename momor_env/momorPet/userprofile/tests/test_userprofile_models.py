from django.test import TestCase
from django.contrib.auth.models import User
# Replace 'yourapp' with your actual app name
from yourapp.models import UserProfile


class UserProfileModelTest(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_userprofile_creation(self):

        user_profile = UserProfile.objects.create(
            user=self.user,
            bio='This is a test bio.',

        )

        saved_profile = UserProfile.objects.get(user=self.user)

        self.assertEqual(saved_profile.user, self.user)
        self.assertEqual(saved_profile.bio, 'This is a test bio.')

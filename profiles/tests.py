from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileTest(APITestCase):
    """
    Tests for profile app
    """

    def setUp(self):
        """
        Function to setup users and create listings
        """
        User.objects.create_user(username='ben', password='pass')
        User.objects.create_user(username='peter', password='word')

    def test_can_list_profiles(self):
        """
        test if profiles can be listed
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.data["count"], 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_profile_with_valid_id(self):
        """
        Test if you could retrieve Profile with valid id
        """
        response = self.client.get('/profiles/1')
        self.assertEqual(response.data['owner'], 'ben')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_profile_with_invalid_id(self):
        """
        Test if you could retrieve Profile with invalid id
        """
        response = self.client.get('/profiles/100')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

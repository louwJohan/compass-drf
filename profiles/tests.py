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

    def test_loggedin_user_can_edit_profile(self):
        """
        Logged in user can edit profile
        """
        self.client.login(username='ben', password='pass')
        response = self.client.put('/profiles/1', {'profile_name': 'Big Ben'})
        self.assertEqual(response.data['profile_name'], 'Big Ben')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_user_can_edit_profile(self):
        """
        Unauthorized user can edit profile
        """
        response = self.client.put('/profiles/1', {'profile_name': 'Big Ben'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

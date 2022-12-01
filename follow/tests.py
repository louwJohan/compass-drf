from django.contrib.auth.models import User
from .models import Follower
from rest_framework import status
from rest_framework.test import APITestCase


class FollowingTest(APITestCase):
    """
    Tests for following models and view
    """
    def setUp(self):
        ben = User.objects.create_user(username='ben', password='pass')
        peter = User.objects.create_user(username='peter', password='word')
        Follower.objects.create(
            owner=User.objects.get(pk=1), followed=User.objects.get(pk=2)
        )

    def test_can_list_following(self):
        """
        Test to list all followed
        """
        response = self.client.get('/following/')
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_loggedin_user_can_follow_other_user(self):
        """
        Test to see if authorized user can follow other user
        """
        self.client.login(username='peter', password='word')
        response = self.client.post('/following/', {'followed': 1})
        self.assertEqual(response.data['followed_name'], 'ben')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_user_can_follow_other_user(self):
        """
        Test to see if unauthorized user can follow other user
        """
        response = self.client.post('/following/', {'followed': 1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_retrieve_followed_item_with_valid_id(self):
        """
        Test to retrieve followed item with id
        """
        response = self.client.get('/following/1')
        self.assertEqual(response.data['followed_name'], 'peter')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_followed_item_with_invalid_id(self):
        """
        Test to retrieve item with invalid id
        """
        response = self.client.get('/following/100')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

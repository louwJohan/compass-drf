from django.contrib.auth.models import User
from listing.models import Listing
from .models import Saved
from rest_framework import status
from rest_framework.test import APITestCase


class SavedTest(APITestCase):
    """
    Tests for saved app
    """
    def setUp(self):
        """
        Function to setup users and create listings
        """
        ben = User.objects.create_user(username='ben', password='pass')
        peter = User.objects.create_user(username='peter', password='word')
        Listing.objects.create(
            owner=ben, title='test1', description='house',
            type_of_property='detached_house', bedrooms='4',
            area='Leeds', price='200000', commerce_type='sell',
            image_one='', image_two='', image_three='', image_four='',
            image_five='', image_six='', image_seven='', image_eight=''
        )
        Listing.objects.create(
            owner=ben, title='test2', description='house2',
            type_of_property='detached_house', bedrooms='5',
            area='Leeds', price='2000000', commerce_type='sell',
            image_one='', image_two='', image_three='', image_four='',
            image_five='', image_six='', image_seven='', image_eight=''
        )
        Saved.objects.create(
            listing=Listing.objects.get(pk=1), owner=User.objects.get(pk=2)
        )

    def test_loggedin_user_can_save_listing(self):
        """
        Logged in user can save a listing
        """
        self.client.login(username='peter', password='word')
        response = self.client.post('/saved/', {'listing': 2})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_user_can_save_listing(self):
        """
        Unauthorized user can save a listing
        """
        response = self.client.post('/saved/', {'listing': 2})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_list_saved_listings(self):
        """
        Test if you can list all saved items
        """
        response = self.client.get('/saved/')
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_saved_detail_with_valid_id(self):
        """
        Test if you can list saved detail with valid id
        """
        response = self.client.get('/saved/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_saved_detail_with_invalid_id(self):
        """
        Test if you can list saved detail with invalid id
        """
        response = self.client.get('/saved/100')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


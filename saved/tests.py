from django.contrib.auth.models import User
from .models import Listing
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

    def test_can_save_listing(self):
        self.client.login(username='peter', password='word')
        response = self.client.post('/saved/', 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
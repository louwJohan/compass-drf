from django.contrib.auth.models import User
from .models import Listing
from rest_framework import status
from rest_framework.test import APITestCase


class ListingListTests(APITestCase):
    """
    Testing listings
    """

    def setUp(self):
        """
        Setup user
        """
        User.objects.create_user(username='ben', password='pass')

    def test_can_list_listings(self):
        """
        Test if you can retrieve Listings
        """
        ben = User.objects.get(username='ben')
        Listing.objects.create(owner=ben, title='Test')
        response = self.client.get('/listings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_listing(self):
        """
        Test if Logged in user can create listing
        """
        self.client.login(username='ben', password='pass')
        response = self.client.post('/listings/', {'title': 'test',
                                                   'description': 'house',
                                                   'type_of_property': 'detached_house',
                                                   'bedrooms': '4',
                                                   'area': 'Leeds',
                                                   'price': '200000',
                                                   'commerce_type': 'sell',
                                                   'image_one': '',
                                                   'image_two': '',
                                                   'image_three': '',
                                                   'image_four': '',
                                                   'image_five': '',
                                                   'image_six': '',
                                                   'image_seven': '',
                                                   'image_eight': ''
                                                   })
        count = Listing.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_create_listing(self):
        """
        Test if unauthorized user can create listing
        """
        response = self.client.post('/listings/', {'title': 'test'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ListingDetailViewTests(APITestCase):
    """
    Tests for the detail view
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

    def test_can_retrieve_listing_using_valid_id(self):
        """
        Test to retrieve listing with and valid id
        """
        response = self.client.get('/listings/1')
        self.assertEqual(response.data['title'], 'test1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_listing_using_invalid_id(self):
        """
        Test if user can retrieve a listing with an invalid id
        """
        response = self.client.get('/listings/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_listing(self):
        """
        Test if user can update listing
        """
        self.client.login(username='ben', password='pass')
        response = self.client.put('/listings/1', {'title': 'new title',
                                                   'description': 'house',
                                                   'type_of_property': 'detached_house',
                                                   'bedrooms': '4',
                                                   'area': 'Leeds',
                                                   'price': '200000',
                                                   'commerce_type': 'sell',
                                                   })
        listing = Listing.objects.filter(pk=1).first()
        self.assertEqual(listing.title, 'new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_update_another_users_listing(self):
        """
        Test if user can update another users listing
        """
        self.client.login(username='peter', password='word')
        response = self.client.put('/listings/1', {'title': 'new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

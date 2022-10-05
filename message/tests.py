from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from listing.models import Listing
from .models import Message


class MessageTests(APITestCase):
    def setUp(self):
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

    def test_logged_in_user_can_create_message(self):
        self.client.login(username='ben', password='pass')
        response = self.client.post('/messages/', {'owner': 'ben',
                                                   'listing': '2',
                                                   'name': 'Ben',
                                                   'surname': 'Owens',
                                                   'email': 'beno@mail.com',
                                                   'phone_number': '09878923456',
                                                   'title': 'Viewing',
                                                   'content': 'Hi I would like to view the property'
                                                   })
        count = Message.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_can_retrieve_listing_using_valid_id(self):
        response = self.client.get('/listings/1')
        self.assertEqual(response.data['title'], 'test1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_can_retrieve_listing_using_invalid_id(self):
#         response = self.client.get('/listings/100/')
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_user_can_update_own_listing(self):
#         self.client.login(username='ben', password='pass')
#         response = self.client.put('/listings/1', {'title': 'new title',
#                                                    'description':'house',
#                                                    'type_of_property': 'detached_house',
#                                                    'bedrooms': '4',
#                                                    'area': 'Leeds', 
#                                                    'price': '200000', 
#                                                    'commerce_type': 'sell',
#                                                     })
#         listing = Listing.objects.filter(pk=1).first()
#         # self.assertEqual(listing.title, 'new title')
#         # self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_can_update_another_users_listing(self):
#         self.client.login(username='peter', password='word')
#         response = self.client.put('/listings/1', {'title': 'new title'})
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

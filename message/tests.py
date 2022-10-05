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

        one = Listing.objects.get(pk=1)
        two = Listing.objects.get(pk=2)

        Message.objects.create(owner=ben,
                               listing=one,
                               name='Ben',
                               surname='Owens',
                               email='beno@mail.com',
                               phone_number='09878923456',
                               title='Viewing',
                               content='Hi I would like to view the property'
                                )
        Message.objects.create(owner=peter,
                               listing=two,
                               name='Peter',
                               surname='Pan',
                               email='pp@mail.com',
                               phone_number='09878923456',
                               title='Viewing',
                               content='Hi I would like to view the property'
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
        self.assertEqual(count, 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_can_retrieve_message_using_valid_id(self):
        self.client.login(username='ben', password='pass')
        response = self.client.get('/messages/1')
        self.assertEqual(response.data['title'], 'Viewing')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_message_using_invalid_id(self):
        response = self.client.get('/messages/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

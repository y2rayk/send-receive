from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myapp.models import Message
from django.contrib.auth import get_user_model
from collections import OrderedDict
from rest_framework.exceptions import ErrorDetail
from unittest import mock
USER_MODEL = get_user_model()

class MessageTests(APITestCase):

    def setUp(self):
        user = self.create_user('sender')
        receiver = self.create_user('receiver')

    def test_unauthenticated_should_403_on_POST(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_should_403_on_GET(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.get(url, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_should_403_on_DELETE(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.delete(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_should_403_on_PATCH(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.patch(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_message_should_create_obj(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        response = self.create_message("hello world!")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expected = {
            'id': 1,
            'sender': OrderedDict([('type', 'User'), ('id', '1')]),
            'text': 'hello world!',
            'receiver': OrderedDict([('type', 'User'), ('id', '1')]),
            'seen': False,
            'pub_date': mock.ANY
        }
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(response.data, expected)

    def test_create_message_to_invalid_user_should_error(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        response = self.create_message("hello world!", receiver_id="999")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected = [
            {
                'detail': ErrorDetail(string='Invalid pk "999" - object does not exist.', code='does_not_exist'),
                'status': '400',
                'source': {
                    'pointer': '/data/attributes/receiver'
                },
                'code': 'does_not_exist'
            }
        ]
        self.assertEqual(Message.objects.count(), 0)

    def test_fetch_no_messages(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        url = reverse('message-list')
        response = self.client.get(url, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Message.objects.count(), 0)
        expected = {
            'results': [],
            'meta': {
                'pagination': OrderedDict([('page', 1), ('pages', 1), ('count', 0)])},
            'links': OrderedDict([('first', 'http://testserver/v1/messages/?page%5Bnumber%5D=1'), ('last', 'http://testserver/v1/messages/?page%5Bnumber%5D=1'), ('next', None), ('prev', None)])
        }
        self.assertEqual(response.data, expected)

    def test_fetch_non_existing_message_should_error(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        url = reverse('message-list')
        response = self.client.get(url + '999/', format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_fetch_range_of_messages(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        response = self.create_message('dont care')
        response = self.create_message('dont care')
        response = self.create_message('dont care')
        response = self.create_message('dont care')
        response = self.create_message('dont care')
        url = reverse('message-list')
        response = self.client.get(url, format='vnd.api+json')
        import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)

    def test_fetch_only_new_messages(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        response = self.create_message('dont care')
        url = reverse('message-list')
        response = self.client.get(url + f'?filter[seen]=false', format='vnd.api+json')
        expected = {
            'results': [OrderedDict([('id', 1), ('sender', OrderedDict([('type', 'User'), ('id', '1')])), ('text', 'dont care'), ('receiver', OrderedDict([('type', 'User'), ('id', '1')])), ('seen', False), ('pub_date', mock.ANY)])],
            'meta': {
                'pagination': OrderedDict([('page', 1), ('pages', 1), ('count', 1)])},
            'links': OrderedDict([('first', 'http://testserver/v1/messages/?filter%5Bseen%5D=false&page%5Bnumber%5D=1'), ('last', 'http://testserver/v1/messages/?filter%5Bseen%5D=false&page%5Bnumber%5D=1'), ('next', None), ('prev', None)])
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

    def test_fetch_one_message_should_have_many_fields(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        response = self.create_message('dont care')
        the_id = response.data['id']
        url = reverse('message-list')
        response = self.client.get(url + f'{the_id}/', format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = {
            'id': 1,
            'sender': OrderedDict([('type', 'User'), ('id', '1')]),
            'text': 'dont care',
            'receiver': OrderedDict([('type', 'User'), ('id', '1')]),
            'seen': False,
            'pub_date':  mock.ANY
        }
        self.assertEqual(response.data, expected)

    def test_delete_message(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        response = self.create_message('dont care')
        the_id = response.data['id']
        url = reverse('message-list')
        response = self.client.delete(url + f'{the_id}/', format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Message.objects.count(), 0)

    def test_delete_non_existing_message_should_error(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        url = reverse('message-list')
        response = self.client.delete(url + '666/', format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_multiple_messages(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url + '666/', data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_delete_non_existing_multiple_messages_should_error(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_set_message_as_seen(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        response = self.create_message('dont care')
        the_id = response.data['id']
        url = reverse('message-list')
        data = {
            "data": {
                "type": "Message",
                "id": the_id,
                "attributes": {
                    "seen": True,
                },
            }
        }
        response = self.client.patch(url + f'{the_id}/', data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected = {
            'id': 1,
            'sender': OrderedDict([('type', 'User'), ('id', '1')]),
            'text': 'dont care',
            'receiver': OrderedDict([('type', 'User'), ('id', '1')]),
            'seen': True,
            'pub_date': mock.ANY
        }
        self.assertEqual(response.data, expected)

    def test_set_message_as_seen_on_non_existing_message_should_error(self):
        sender = USER_MODEL.objects.get(username='sender')
        self.client.force_authenticate(user=sender)
        the_id = 888
        url = reverse('message-list')
        data = {
            "data": {
                "type": "Message",
                "id": the_id,
                "attributes": {
                    "seen": True,
                },
            }
        }
        response = self.client.patch(url + f'{the_id}/', data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def create_user(self, username):
        user = USER_MODEL.objects.create(username=username, password='password')

    def create_message(self, text, receiver_id="1"):
        url = reverse('message-list')
        data = {
            "data": {
                "type": "Message",
                "attributes": {
                    "text": text,
                    "seen": False,
                    "pub_date": "2021-05-24T01:58:17.177290Z"
                },
                "relationships": {
                    "sender": {
                        "data": {
                            "type": "User",
                            "id": "1"
                        }
                    },
                    "receiver": {
                        "data": {
                            "type": "User",
                            "id": receiver_id
                        }
                    }
                }
            }
        }
        response = self.client.post(url, data, format='vnd.api+json')
        return response

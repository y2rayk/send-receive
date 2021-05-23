from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myapp.models import Message

class MessageTests(APITestCase):

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
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')

    def test_create_message_to_invalid_user_should_error(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')

    def test_create_message_to_invalid_user_should_error(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')

    def test_fetch_no_messages(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_fetch_non_existing_message_should_error(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_fetch_range_of_messages(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_fetch_only_new_messages(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_fetch_one_message_should_have_many_fields(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_delete_message(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_delete_non_existing_message_should_error(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_delete_multiple_messages(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_delete_non_existing_multiple_messages_should_error(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_set_message_as_seen(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

    def test_set_message_as_seen_on_non_existing_message_should_error(self):
        url = reverse('message-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='vnd.api+json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().name, 'DabApps')
        1/0

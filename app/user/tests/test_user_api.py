from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
USER_PAYLOAD = {
    'email': 'test_api@geo4cities.com',
    'password': 'Valid_Password',
    'name': 'Full Test User Name',
}


class PublicUserApiTests(TestCase):
    """Tests the users API (public)"""

    def setUp(self):
        self.user = APIClient()

    def test_create_user_success(self):
        """Test creating user with valid payload is successful"""
        res = self.client.post(CREATE_USER_URL, USER_PAYLOAD)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)

        self.assertTrue(user.check_password(USER_PAYLOAD['password']))
        self.assertNotIn('password', res.data)

    def test_create_user_exists(self):
        """Test creating a user that already exists fails"""
        get_user_model().objects.create_user(**USER_PAYLOAD)
        res = self.client.post(CREATE_USER_URL, USER_PAYLOAD)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_password_too_short(self):
        """Test that password must be more than 4 characters"""
        payload = dict(USER_PAYLOAD, password='1234')
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

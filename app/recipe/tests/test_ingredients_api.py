from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient

from recipe.serializers import IngredientSerializer


INGREDIENTS_URL = reverse('recipe:ingredient-list')


class PublicIngredientsApiTests(TestCase):
    """Test the public ingredients api"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving ingredients"""
        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateIngredientsApiTests(TestCase):
    """Test the authorized user ingredients api"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@geo4cities.com',
            'valid_password',
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieving_ingredients(self):
        """Test that authenticated user can retrieve ingredients"""
        Ingredient.objects.create(user=self.user, name='Kale')
        Ingredient.objects.create(user=self.user, name='Salt')

        ingredient = Ingredient.objects.all().order_by('-name')
        serializer = IngredientSerializer(ingredient, many=True)

        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieving_ingredients_limited_to_user(self):
        """Test that ingredients are returned are for authenticated user"""
        user2 = get_user_model().objects.create_user(
            'other@geo4cities.com',
            'valid_password',
        )

        Ingredient.objects.create(user=user2, name='Vinegar')
        ingredient = Ingredient.objects.create(user=self.user, name='Tumeric')

        res = self.client.get(INGREDIENTS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)

    # def test_create_tag_successful(self):
    #     """Test creating a new tag"""
    #     payload = {'name': 'Test Tag'}
    #     self.client.post(TAGS_URL, payload)
    #
    #     exists = Tag.objects.filter(
    #         user=self.user,
    #         name=payload['name'],
    #     ).exists()
    #
    #     self.assertTrue(exists)
    #
    # def test_create_tag_invalid(self):
    #     """Test creating a new tag with invalid payload"""
    #     payload = {'name': ''}
    #     res = self.client.post(TAGS_URL, payload)
    #
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

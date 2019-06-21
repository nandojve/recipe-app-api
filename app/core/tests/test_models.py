from django.test import TestCase
from django.contrib.auth import get_user_model

from unittest.mock import patch

from core import models


def sample_user(email='test@geo4cities.com', password='valid_password'):
    """Create sample user to be used in test cases"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@geo4cities.com'
        password = '12345678Test'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GEO4CITIES.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='12345678Test'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raizes error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """test creationg a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@geo4cities.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredients_str(self):
        """Test the ingredients string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Stake and mushroom sauce',
            time_minutes=5,
            price=5.01,
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'my_image.jpg')
        expected_path = f'uploads/recipes/{uuid}.jpg'
        self.assertEqual(file_path, expected_path)

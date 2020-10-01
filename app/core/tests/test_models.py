from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "test@xyz.com"
        password = "test5156"
        user = get_user_model().objects.create_user(
        email=email,
        password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):
        email = "abc@YAHOO.COM"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_email_validation(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_issuperuser(self):
        user = get_user_model().objects.create_superuser('test@xyz.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

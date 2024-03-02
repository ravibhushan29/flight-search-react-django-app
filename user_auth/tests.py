from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
from user_auth.models import UserProfile


class AuthTestCase(APITestCase):

    def setUp(self):
        """
        Create a user for login tests
        login_url and signup_url setup
        """
        self.user = UserProfile.objects.create(
            username="ravi_test_user",
            password=make_password("ravi@password123"),
            first_name="Test",
            last_name="User",
        )

        self.login_url = reverse("user-login")
        self.signup_url = reverse("user-signup")

    def test_login_empty_payload(self):
        response = self.client.post(self.login_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_login(self):
        data = {"username": "ravi_test_user", "password": "ravi@password123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_invalid_username(self):
        data = {"username": "ravi_test_user2673687", "password": "ravi@password123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_incorrect_password(self):
        data = {"username": "ravi_test_user", "password": "ravi@pass"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successful_signup(self):
        data = {
            "username": "ravi.raj",
            "password": "ravi@45678",
            "first_name": "Ravi",
            "last_name": "Raj",
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("token", response.data)

    def test_duplicate_username_signup(self):
        data = {
            "username": "ravi_test_user",  # this username is already exists
            "password": "abcd@hdj@123",
            "first_name": "Ravi",
            "last_name": "Bhushan",
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

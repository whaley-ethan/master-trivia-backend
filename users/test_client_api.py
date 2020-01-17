from django.test import TestCase
from rest_framework.test import APIClient

class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = {"username": "JonDoe", "email": "jon@doe.com",
                     "password1": "testpassword1", "password2": "testpassword1"}
        self.badPasswordUser = {"username": "JonDoe", "email": "jon@doe.com",
                                "password1": "testpassword1", "password2": "anotherPassword2"}

    def test_create_valid_user(self):
        response = self.client.post(
            "/api/rest-auth/registration/", self.user, format="json")
        # httpCode 201 -> "created"
        self.assertEqual(response.status_code, 201)
        # should get same key back when logging in
        response2 = self.client.post(
            "/api/rest-auth/login/", {"username": "JonDoe", "email": "jon@doe.com", "password": "testpassword1"})
        self.assertEqual(response.data, response2.data)

    def test_create_nonmatching_passwords(self):
        response = self.client.post(
            "/api/rest-auth/registration/", self.badPasswordUser, format="json")
        # httpCode 400 -> "Bad Request"
        self.assertEqual(response.status_code, 400)

    def test_login_and_logout(self):
        pass

    def test_relationship_display(self):
        response = self.client.post(
            "/api/rest-auth/login/", {"username": "JonDoe", "email": "jon@doe.com", "password": "testpassword1"})
        user_id = response.json()

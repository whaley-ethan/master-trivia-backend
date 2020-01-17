from django.core.exceptions import ValidationError
from django.test import TestCase
from rest_framework.test import APIClient
from users.views import UserListView

from .models import Quiz
from .models import Answer
from users.models import CustomUser


class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = {"username": "JonDoe", "email": "jon@doe.com",
                     "password1": "testpassword1", "password2": "testpassword1"}
        self.badPasswordUser = {"username": "JonDoe", "email": "jon@doe.com",
                                "password1": "testpassword1", "password2": "anotherPassword2"}

    def testCreateValidUser(self):
        response = self.client.post(
            "/api/rest-auth/registration/", self.user, format="json")
        # httpCode 201 -> "created"
        self.assertEqual(response.status_code, 201)
        # should get same key back when logging in
        response2 = self.client.post(
            "/api/rest-auth/login/", {"username": "JonDoe", "email": "jon@doe.com", "password": "testpassword1"})
        self.assertEqual(response.data, response2.data)

    def testCreateNonMatchingPasswords(self):
        response = self.client.post(
            "/api/rest-auth/registration/", self.badPasswordUser, format="json")
        # httpCode 400 -> "Bad Request"
        self.assertEqual(response.status_code, 400)

class QuizAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = {"username": "JonDoe", "email": "jon@doe.com",
                     "password1": "testpassword1", "password2": "testpassword1"}
        self.client.post("/api/rest-auth/registration/",
                         self.user, format="json")

    def testCreateQuiz(self):
        response = self.client.post("/api/quiz/")
        self.assertEqual(response.status_code, 201)
        parsed_response = response.json()
        id = parsed_response['id']
        response2 = self.client.get(f"/api/quiz/{id}/")
        self.assertEqual(response2.status_code, 200)

    def testAddAnswerToQuiz(self):
        response = self.client.post("/api/quiz/")
        parsed_response = response.json()
        id = parsed_response['id']
        test_answer = {
            "quiz": id,
            "category": "General Knowledge",
            "difficulty": "easy",
            "didGetRight": "true",
            "time": "5000"
        }
        response2 = self.client.post("/api/answer/", test_answer, format="json")
        self.assertEqual(response2.status_code, 201)
        response3 = self.client.get(f"/api/quiz/{id}/")
        response3_answers = response3.json()[0]['answers']
        self.assertEqual(response3_answers[0], 'right easy General Knowledge 5000')

    def testStatisticsDataFromQuiz(self):
        pass

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
        self.user = { "username": "JonDoe", "email": "jon@doe.com", "password1":"testpassword1", "password2": "testpassword1" }
        self.badPasswordUser = { "username": "JonDoe", "email": "jon@doe.com", "password1":"testpassword1", "password2": "anotherPassword2" }
    
    def testCreateValidUser(self):
        response = self.client.post("/api/rest-auth/registration/", self.user, format="json")
        self.assertEqual(response.status_code, 201) # httpCode 201 -> "created"
        response2 = self.client.post("/api/rest-auth/login/", {"username": "JonDoe", "email": "jon@doe.com", "password": "testpassword1" }) #should get same key back when logging in
        self.assertEqual(response.data, response2.data)
    
    def testCreateNonMatchingPasswords(self):
        response = self.client.post("/api/rest-auth/registration/", self.badPasswordUser, format="json")
        self.assertEqual(response.status_code, 400) # httpCode 400 -> "Bad Request"

class QuizTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = {"username": "JonDoe", "email": "jon@doe.com", "password1":"testpassword1", "password2": "testpassword1" }
        self.client.post("/api/rest-auth/registration/", self.user, format="json")
    
    def testCreateQuiz(self):
        #learn how to use current logged in user as default user, modify code to do so (TDD, write the test first then write the code)
        pass

    def testAddAnswerToQuiz(self):
        pass

    def testStatisticsDataFromQuiz(self):
        pass
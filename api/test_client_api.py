from django.test import TestCase
from rest_framework.test import APIClient

class QuizAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = {"username": "JonDoe", "email": "jon@doe.com",
                     "password1": "testpassword1", "password2": "testpassword1"}
        self.client.post("/api/rest-auth/registration/",
                         self.user, format="json")

    def test_create_quiz(self):
        response = self.client.post("/api/quiz/")
        self.assertEqual(response.status_code, 201)
        parsed_response = response.json()
        id = parsed_response['id']
        response2 = self.client.get(f"/api/quiz/{id}/")
        self.assertEqual(response2.status_code, 200)

    def test_add_answer_to_quiz(self):
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

    def test_statistics_data_from_quiz(self):
        pass

from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Quiz
from .models import Answer
from users.models import CustomUser
# Create your tests here.

class QuizModelTests(TestCase):
    def setUp(self):
        self.user1 = CustomUser(name='Jon Doe', email='jdoe@email.com')
        self.user1.save()
        self.quiz1 = Quiz(user=self.user1)
        self.quiz1.save()
        self.answer1 = Answer(quiz=self.quiz1, category="General Knowledge", difficulty = "easy", time = 5000, didGetRight = True) 

    def test_new_quiz_adding_answer(self):
        """ creating a new quiz and adding an answer stores answer correctly
        """
        self.assertEqual(len(self.quiz1.answers.all()), 0)  # new quiz should have no answers
        self.answer1.save()                                 # until we save the first answer
        quiz1Answers = self.quiz1.answers.all()
        self.assertEqual(quiz1Answers[0], self.answer1)
        self.assertEqual(quiz1Answers[0].difficulty, "easy")
        self.assertEqual(quiz1Answers[0].time, 5000)


class AnswerModelTests(TestCase):
    def setUp(self):
        self.user1 = CustomUser(name='Jon Doe', email='jdoe@email.com')
        self.user1.save()
        self.quiz1 = Quiz(user=self.user1)
        self.quiz1.save()

    def test_new_answer_with_bad_category(self):
        answer = Answer(quiz=self.quiz1, category="This Is Not A Valid Category", difficulty = "easy", time = 5000, didGetRight = True)
        with self.assertRaises(ValidationError):
            answer.save()

    def test_new_answer_with_bad_difficulty(self):
        answer = Answer(quiz=self.quiz1, category="General Knowledge", difficulty = "extra hard", time = 5000, didGetRight = True)
        with self.assertRaises(ValidationError):
            answer.save()
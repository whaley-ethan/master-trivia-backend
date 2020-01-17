from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Quiz
from .models import Answer
from users.models import CustomUser
# Create your tests here.

class QuizModelTests(TestCase):
    def setUp(self):
        self.user = CustomUser(name='Jon Doe', email='jdoe@email.com')
        self.user.save()
        self.quiz = Quiz(user=self.user)
        self.quiz.save()
        self.answer = Answer(quiz=self.quiz, category="General Knowledge", difficulty = "easy", time = 5000, didGetRight = True) 

    def test_new_quiz_adding_answer(self):
        """ creating a new quiz and adding an answer stores answer correctly
        """
        self.assertEqual(len(self.quiz.answers.all()), 0)  # new quiz should have no answers
        self.answer.save()                                 # until we save the first answer
        quizAnswers = self.quiz.answers.all()
        self.assertEqual(len(quizAnswers), 1) 
        self.assertEqual(quizAnswers[0], self.answer)
        self.assertEqual(quizAnswers[0].difficulty, "easy")
        self.assertEqual(quizAnswers[0].time, 5000)


class AnswerModelTests(TestCase):
    def setUp(self):
        self.user = CustomUser(name='Jon Doe', email='jdoe@email.com')
        self.user.save()
        self.quiz = Quiz(user=self.user)
        self.quiz.save()
        self.answerBadCategory = Answer(quiz=self.quiz, category="Code Without Tests", difficulty = "easy", time = 5000, didGetRight = True)
        self.answerBadDifficulty = Answer(quiz=self.quiz, category="General Knowledge", difficulty = "extra hard", time = 5000, didGetRight = True)

    def test_new_answer_with_bad_category(self):
        with self.assertRaises(ValidationError):
            self.answerBadCategory.save()

    def test_new_answer_with_bad_difficulty(self):
        with self.assertRaises(ValidationError):
            self.answerBadDifficulty.save()
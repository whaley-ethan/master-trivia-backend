from .models import Answer, Quiz
from .serializers import AnswerSerializer, QuizSerializer
from rest_framework import generics

# Create your views here.
class AnswerListCreate(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class QuizListCreate(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
from rest_framework import serializers
from .models import Answer, Quiz

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('quiz', 'category', 'difficulty', 'didGetRight', 'time')

class QuizSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    answers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ('id', 'user', 'answers')
from api.models import Answer, Quiz
from django.db.models import Count
from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id','email', 'username', )

class UserStaticsicsSerializer(serializers.ModelSerializer):
    five_fastest_right_answers = serializers.SerializerMethodField()
    five_best_categories = serializers.SerializerMethodField()
    favorite_category = serializers.SerializerMethodField()

    class Meta:
        model = models.CustomUser
        read_only_fields = ('five_fastest_right_answers',)
        fields = ('id', 'username','five_fastest_right_answers', 'favorite_category', 'five_best_categories')
    
    def get_all_user_quizes(self, obj):
        return [quiz.id for quiz in obj.quizes.all()]

    def get_category_counts(self, obj):
        all_user_quizes = self.get_all_user_quizes(obj)
        user_categories = Answer.objects.filter(quiz__in=all_user_quizes).values("category").annotate(Count("id"))
        return user_categories

    def get_five_fastest_right_answers(self, obj):
        all_user_quizes = self.get_all_user_quizes(obj)
        up_to_five_right_answers = Answer.objects.filter(quiz__in=all_user_quizes, didGetRight=True).order_by('time')[:5].all()
        up_to_five = [{'category': answer.category, 'time': answer.time} for answer in up_to_five_right_answers]
        return up_to_five

    def get_favorite_category(self, obj):
        return self.get_category_counts(obj)[:1]

    def get_five_best_categories(self, obj):
        return 42
        # filter answers to those associated with this user through quizes.
        # sort by count by unique category, where didGetRight == True / (count by unique category) limit 5
        # return object {answer.key : answer.calculated_time for answer in filtered list }
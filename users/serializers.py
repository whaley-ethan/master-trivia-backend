from rest_framework import serializers
from . import models
from api.models import Answer, Quiz

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id','email', 'username', )

class UserStaticsicsSerializer(serializers.ModelSerializer):
    top_five_times = serializers.SerializerMethodField()
    top_five_categories = serializers.SerializerMethodField()

    class Meta:
        model = models.CustomUser
        read_only_fields = ('top_five_times',)
        fields = ('id', 'username','top_five_times', 'top_five_categories', )
    
    def get_top_five_times(self, obj):
        all_user_quizes = [quiz.id for quiz in obj.quizes.all()]
        up_to_five_user_answers = Answer.objects.filter(quiz__in=all_user_quizes).order_by('time')[:5].all()
        up_to_five_times = [answer.time for answer in up_to_five_user_answers]
        return up_to_five_times
    
    def get_top_five_categories(self, obj):
        all_user_quizes = [quiz.id for quiz in obj.quizes.all()]
        up_to_five_user_answers = Answer.objects.filter(quiz__in=all_user_quizes).order_by('time')[:5].all()
        up_to_five_categories = [answer.category for answer in up_to_five_user_answers]
        return up_to_five_categories
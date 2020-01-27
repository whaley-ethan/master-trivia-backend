from rest_framework import generics

from . import models
from api.models import Answer
from api.models import Quiz
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserStatisticsListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserStaticsicsSerializer

class UserStatisticsDetailView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserStaticsicsSerializer
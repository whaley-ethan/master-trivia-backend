from rest_framework import generics
from django.http import JsonResponse
from django.middleware.csrf import get_token

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

class UserStatisticsDetailView(generics.RetrieveAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserStaticsicsSerializer

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('statistics/', views.UserStatisticsListView.as_view()),
    path('statistics/<int:pk>/', views.UserStatisticsDetailView.as_view()),
]
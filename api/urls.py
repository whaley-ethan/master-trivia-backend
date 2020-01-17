from django.urls import include, path
from . import views

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('quiz/', views.QuizListCreate.as_view() ),
    path('quiz/<int:pk>/', views.QuizDetail.as_view() ),
    path('answer/', views.AnswerListCreate.as_view() ),
]
from django.urls import path, include
from .views import helloApi, randomQuiz, index
from . import views
from rest_framework import urls

urlpatterns  =[
    path("hello", helloApi),
    path("<int:id>/", randomQuiz),
    path("index", index),
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
from django.urls import path, include
from .views import helloApi, randomQuiz

urlpatterns  =[
    path("hello", helloApi),
    path("<int:id>/", randomQuiz),
]
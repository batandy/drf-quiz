import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
from django.http import HttpResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import generics

@api_view(['GET'])
def helloApi(request):
    return Response("hello")


@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)

def index(request):
    return render(request, 'index.html')

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
import random
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz, Question, Category
from .serializers import *
from django.http import HttpResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework import status


@api_view(['GET'])
def helloApi(request):
    return Response("hello")


@api_view(['GET'])
def quiz_detail(request, cat_id, quiz_id):
    try:
        questions = Question.objects.filter(category_id=cat_id, quiz_id=quiz_id)
    except Quiz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def category_detail(request, cat_id):
    try:
        category= Category.objects.get(category_id=cat_id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    

@api_view(['GET'])
def only_category(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = OnlyCategorySerializer(categorys, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def only_quiz(request,cat_id):
    if request.method == 'GET':
        quizzes = Quiz.objects.filter(category_id=cat_id)
        serializer = OnlyQuizSerializer(quizzes, many=True)
        return Response(serializer.data)





class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
import random
from django.shortcuts import get_object_or_404, render
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
def all_quizs(request):
    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
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



class createQuiz(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = CreateQuizSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quiz = self.perform_create(serializer)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        quiz = serializer.save()
        return quiz



class createQuestion(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = CreateQuestionSerializer

    def get(self, request, quiz_id):
        queryset = Question.objects.filter(quiz_id=quiz_id)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, quiz_id, *args, **kwargs):
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        data = request.data.copy()
        data['category'] = quiz.category_id  # category_id 자동 할당
        data['quiz']=quiz.pk
        serializer = self.get_serializer(data=data)

        serializer.is_valid(raise_exception=True)
        question = self.perform_create(serializer)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        question = serializer.save()
        return question

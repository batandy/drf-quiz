from rest_framework import serializers
from .models import Quiz, Question, Category
from .models import User


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model =Question
        fields = ('title', 'body', 'answer')

class QuizSerializer(serializers.ModelSerializer):
    questions= QuestionSerializer(many=True)
    class Meta:
        model=Quiz
        fields = ('category', 'quiz_name', 'quiz_id', 'questions')

class CategorySerializer(serializers.ModelSerializer):
    quizs = QuizSerializer(many=True)
    class Meta:
        model=Category
        fields = ('category_name','category_id', 'quizs')

class OnlyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ('category_name','category_id')

class OnlyQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields = ('quiz_name', 'quiz_id')




class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            nickname = validated_data['nickname'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['nickname', 'email', 'name', 'password']
from rest_framework import serializers
from users.models import User
from core.models import Question, Answer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email',]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields =[
            'author',
            'question',
            'text',
            'date',
        ]

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True, required=False)
    class Meta:
        model = Question
        fields =[
            'url',
            'user',
            'title',
            'body',
            'date',
            'answers',
        ]


from rest_framework import serializers
from users.models import User
from core.models import Question

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'is_staff']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
 
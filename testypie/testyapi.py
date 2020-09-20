from tastypie.resources import ModelResource
from core.models import Question, Answer
from users.models import User


class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'

class AnswerResource(ModelResource):
    class Meta:
        queryset = Answer.objects.all()
        resource_name = 'answer'

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
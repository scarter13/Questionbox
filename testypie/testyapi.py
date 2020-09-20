from tastypie.resources import ModelResource
from core.models import Question, Answer


class QuestionResource(ModelResource):
    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'

class AnswerResource(ModelResource):
    class Meta:
        queryset = Answer.objects.all()
        resource_name = 'answers'
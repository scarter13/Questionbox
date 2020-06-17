from django.db import models
from users.models import User


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, null=True, related_name = 'questions')
    headline = models.CharField(max_length = 255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, null=True, related_name = 'answers')
    question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = 'answers')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class StarQuestion(models.Model):
    user = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name = 'star_questions')
    


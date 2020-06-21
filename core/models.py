from django.db import models
from users.models import User
from django.contrib.postgres.search import SearchQuery, SearchVector


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='questions')
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


class Answer(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='answers')
    question = models.ForeignKey(to = Question, on_delete = models.CASCADE, related_name='answers')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #correct = models.BooleanField(blank=True, null=True)
    
    class Meta:
        ordering = ['-date']

class StarQuestion(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='star_questions')
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, null=True)
    star = models.BooleanField(blank=True, null=True)

class StarAnswer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='star_answers')
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, null=True)
    star = models.BooleanField(blank=True, null=True)
    


from django import forms
from .models import Question
from .models import Answer
from .models import StarQuestion
from .models import StarAnswer
""" 
Uncertain as to whether or not we will actually need a form for the two Star models
"""

class QuestionForm(forms.ModelForm):
    #tag_names = forms.CharField(label="Tags", help_text="Enter tags seperated by spaces.")

    class Meta:
        model = Question
        fields = [
            'title',
            'body',
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'text',
        ]
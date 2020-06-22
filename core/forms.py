from django import forms
from .models import Question
from .models import Answer



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
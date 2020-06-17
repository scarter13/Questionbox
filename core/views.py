from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User
from django.db.models import Q

"""
Import other models as needed from .models and .forms or they won't work!
"""
# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect (to='my_qbox')

    return render(request, "qbox/home.html")



def my_qbox(request):
    questions = request.user.questions.all()
    #answers = request.user.answers.all
    return render(request, "questionbox/my_questionbox.html", {"questions": questions})
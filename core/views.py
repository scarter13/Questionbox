from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.models import User
#from .models import Tag
from .models import Question
from .models import Answer
from .forms import QuestionForm 
from .forms import AnswerForm
from django.db.models import Q


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect (to='my_qbox')

    return render(request, "qbox/home.html")

def my_qbox(request):
    questions = request.user.questions.all()
    answers = request.user.answers.all
    return render(request, "qbox/my_qbox.html", {"questions": questions, "answers": answers})

def create_question(request):
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            #question.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='my_qbox')
    else:
        form = QuestionForm()

    return render(request, "qbox/create_question.html", {"form": form})

def show_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    request_user = request.user
    answers = question.answers.all()

    return render(request, "qbox/show_question.html", {"question": question, "request_user": request_user, "answers": answers})  

def create_answer(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            #question.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='show_question', question_pk=question.pk)
    else:
        form = AnswerForm()

    return render(request, "qbox/create_answer.html", {"form": form, "question": question})

def search_questions(request):
    query = request.GET.get('q')
    if query is not None:
        found_questions = Question.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).distinct()
    else:
        found_questions = None
    return render(request, "qbox/search_questions.html", {"found_questions": found_questions, "query": query})
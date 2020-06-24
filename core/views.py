from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from .models import Question
from .models import Answer
from .forms import QuestionForm 
from .forms import AnswerForm
from django.db.models import Q, Count
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.http import JsonResponse
"""
I'm confused about the SearchQuery and SearchVector.  I noticed on the Clinton's Recipe example that these imports are made at the model level.  Q, on the other hand, is on both models and views.
"""


# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect (to='my_qbox')

    return render(request, "qbox/home.html")

@login_required
def my_qbox(request):
    questions = request.user.questions.all()
    questions = questions.annotate(num_answers=Count('answers'))
    answers = request.user.answers.all()
    answers = answers.distinct('question')

#        search_results = search_results.annotate(search=SearchVector('title', 'body', 'answers__text')).filter(search=query).distinct('pk')
    
    return render(request, "qbox/my_qbox.html", {"questions": questions, "answers": answers})


@login_required
def create_question(request):
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect(to='my_qbox')
    else:
        form = QuestionForm()

    return render(request, "qbox/create_question.html", {"form": form})


def show_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    request_user = request.user
    answers = question.answers.all()
    is_user_favorite = request.user.is_favorite_question(question_pk)

    return render(request, "qbox/show_question.html", {"question": question, "request_user": request_user, "answers": answers, "is_user_favorite": is_user_favorite})  

@login_required
@csrf_exempt
def toggle_favorite_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    if request.user.is_favorite_question(question_pk):
        request.user.favorite_questions.remove(question)
        return JsonResponse({"isFavorite": False})
    else:
        request.user.favorite_questions.add(question)
        return JsonResponse({"isFavorite": True})

"""
Considering how to best build a favorite questions view, method, and work into template
First, to avoid confusion, I think you should change the names of all instances of 'is_user_favorite' to 'is_user_favorite_question."  Or, you could just continue forward with the new field as 'is_user_favorite_answer.'  This would allow for you to differentiate from 'is_user_correct_answer' later on.

@login_required
@csrf_exempt
def toggle_favorite_answer(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)

    if request.user.is_favorite_answer(answer_pk):
        request.user.favorite_answers.remove(answer)
        return JsonResponse({"isFavorite": False})
    else:
        request.user.favorite_answer.add(answer)
        return JsonResponse({"isFavorite": True})

"""

@login_required
def edit_question(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == 'POST':
        form = QuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return redirect(to='show_question', question_pk=question.pk)
    else:
        form = QuestionForm(instance=question)


    return render (request, "qbox/edit_question.html", {"form": form, "question": question})

@login_required
def create_answer(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect(to='show_question', question_pk=question.pk)
    else:
        form = AnswerForm()

    return render(request, "qbox/create_answer.html", {"form": form, "question": question})

def search_questions(request):
    query = request.GET.get('q')

    if query is not None:
        #search_results = Question.objects.filter(Q(title__search=query) | Q(body__search=query)).distinct()
        search_results = Question.objects.all()
        search_results = search_results.annotate(search=SearchVector('title', 'body', 'answers__text')).filter(search=query).distinct('date')
    else:
        search_results = None
    return render(request, "qbox/search_questions.html", {"search_results": search_results, "query": query or ""})
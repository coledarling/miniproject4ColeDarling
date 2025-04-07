from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Question
from .forms import QuizForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    return render(request, 'login.html')

def quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            answer = request.POST.get(f'question_{question.id}')
            if answer and answer.strip().lower() == question.answer.lower():
                score += 1
        request.session['score'] = score
        request.session['total'] = len(questions)
        return redirect('results')
    return render(request, 'quiz.html', {'questions': questions})

def results(request):
    score = request.session.get('score', 0)
    total = request.session.get('total', 0)
    return render(request, 'results.html', {'score': score, 'total': total})
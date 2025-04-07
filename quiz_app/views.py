'''
INF601 - Programming in Python
Assignment# MiniProject 2
I, Cole Darling, affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz_app:quiz')  # Redirect to quiz page after registering
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz_app:quiz')  # Redirect to quiz page after logging in
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('quiz_app:home')  # Redirect to home page after logging out

def quiz(request):
    # Hardcoded questions for the quiz
    questions = [
        {"id": 1, "text": "What is 2 + 2?", "answer": "4"},
        {"id": 2, "text": "What is the capital of France?", "answer": "Paris"},
        {"id": 3, "text": "What color is the sky?", "answer": "Blue"}
    ]

    if request.method == 'POST':
        score = 0
        for question in questions:
            user_answer = request.POST.get(f'question_{question["id"]}', '').strip().lower()
            if user_answer == question["answer"].lower():
                score += 1
        request.session['score'] = score
        request.session['total'] = len(questions)
        return redirect('quiz_app:results')  # Redirect to results page

    return render(request, 'quiz.html', {'questions': questions})

def results(request):
    score = request.session.get('score', 0)
    total = request.session.get('total', 0)
    return render(request, 'results.html', {'score': score, 'total': total})
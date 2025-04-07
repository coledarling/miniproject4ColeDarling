from django.urls import path
from . import views

app_name = 'quiz_app'

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),  # Register page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout action
    path('quiz/', views.quiz, name='quiz'),  # Quiz page
    path('results/', views.results, name='results'),  # Results page
]
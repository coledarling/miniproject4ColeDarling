from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Stores the question
    answer = models.CharField(max_length=100)  # Stores the correct answer

    def __str__(self):
        return self.question_text
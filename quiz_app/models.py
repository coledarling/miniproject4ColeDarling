from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text
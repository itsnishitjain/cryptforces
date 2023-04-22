from django.db import models
from django.contrib.auth.models import AbstractUser
from cryptic.models import Question

class CustomUser(AbstractUser):
    points = models.IntegerField(default=0)
    question_solved = models.ManyToManyField(Question, blank=True)

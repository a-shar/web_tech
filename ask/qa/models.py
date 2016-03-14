from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now())
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

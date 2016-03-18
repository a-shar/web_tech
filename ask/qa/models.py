from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True, default=0)
    author = models.ForeignKey(User, related_name='author')
    likes = models.ManyToManyField(User, related_name="likes")

    def get_url(self):
        return '/question/{0}/'.format(self.id)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

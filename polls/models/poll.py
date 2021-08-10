from django.db import models

from polls.models.question import Question
from django.contrib.auth.models import User


class Poll(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    describe = models.CharField(max_length=1000)
    questions = models.ManyToManyField(Question, related_name='polls', default=None, blank=True)

    def __str__(self):
        return self.name


class CompletedPoll(models.Model):
    poll = models.ForeignKey(Poll, related_name='completed_polls',
                             default=None, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='polls', null=True, blank=True, on_delete=models.CASCADE)

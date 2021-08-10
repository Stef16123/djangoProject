from django.db import models
from polls.models.question import Question
from polls.models.poll import Poll, CompletedPoll
from django.contrib.auth.models import User


class Answer(models.Model):
    text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    poll = models.ForeignKey(Poll, default=None, related_name='answers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='answers', null=True, blank=True, default=None, on_delete=models.CASCADE)
    completed_poll = models.ForeignKey(CompletedPoll, blank=True, related_name='answers', default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

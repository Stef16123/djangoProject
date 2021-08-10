from django.db import models


class Question(models.Model):
    TEXT_OPTION = 'TEXT_OPTION'
    ONE_OPTION = 'ONE_OPTION'
    MANY_OPTION = 'MANY_OPTION'

    TYPE_CHOICES = (
        (TEXT_OPTION, 'text option'),
        (ONE_OPTION, 'one option'),
        (MANY_OPTION, 'many option'),
    )

    text = models.CharField(max_length=200)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

    def __str__(self):
        return self.text

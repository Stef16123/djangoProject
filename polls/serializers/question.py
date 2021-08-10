from rest_framework import serializers
from polls.models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'type', 'polls']

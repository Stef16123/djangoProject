from rest_framework import serializers
from polls.models.answer import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'text', 'question', 'poll', 'user', 'completed_poll']


class AnswerHistorySerializer(serializers.ModelSerializer):
    question_name = serializers.CharField(max_length=600)

    class Meta:
        model = Answer
        fields = ['id', 'text', 'question_id', 'question_name', 'poll_id', 'user_id']

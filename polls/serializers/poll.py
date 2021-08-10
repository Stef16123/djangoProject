from rest_framework import serializers

from polls.models.poll import Poll, CompletedPoll
from polls.serializers.user import UserSerializer
from polls.serializers.answer import AnswerSerializer


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ['id', 'name', 'start_date', 'end_date', 'describe', 'questions']


class CompletedPollSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    isAnon = serializers.BooleanField(default=False)

    class Meta:
        model = CompletedPoll
        fields = ['poll', 'isAnon', 'answers']


class CompletedPollDetailSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = CompletedPoll
        fields = ['poll', 'user', 'answers']
        depth = 2

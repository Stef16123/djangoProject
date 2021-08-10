from django.contrib.auth.models import User
from django.db.models import F
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers.user import UserSerializer
from polls.models.poll import Poll, CompletedPoll
from polls.serializers.poll import PollSerializer, CompletedPollSerializer, CompletedPollDetailSerializer
from polls.models.question import Question
from polls.serializers.question import QuestionSerializer
from polls.models.answer import Answer
from polls.serializers.answer import AnswerSerializer, AnswerHistorySerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if instance.start_date:
            return Response({'status': 'start_data is set'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def get_active_polls(self, request):
        active_polls = Poll.objects.filter(end_date__gte=timezone.now(), start_date__lte=timezone.now())
        serializer = self.get_serializer(active_polls, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def complete_poll(self, request, pk=None):
        serializer = CompletedPollSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user_id = request.user.id if not serializer.data['isAnon'] else None
        completed_poll = CompletedPoll.objects.create(poll_id=serializer.data['poll'], user_id=user_id)
        answers = [Answer(poll_id=serializer.data['poll'],
                          user_id=user_id,
                          text=answer['text'],
                          completed_poll=completed_poll,
                          question_id=answer['question']) for answer in serializer.data['answers']]
        Answer.objects.bulk_create(answers)
        return Response({'status': 'poll completed'})


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(detail=False)
    def get_user_history(self, request):
        self.serializer_class = AnswerHistorySerializer
        if 'user_id' not in request.query_params:
            return Response({'status': 'details'}, status=status.HTTP_404_NOT_FOUND)
        user_id = request.query_params['user_id'] if request.query_params['user_id'] else None
        answers = Answer.objects.filter(user_id=user_id).order_by('poll') \
            .annotate(question_name=F('question__text')).values()
        serializer = self.get_serializer(answers, many=True)
        return Response(serializer.data)


class CompletedPollViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CompletedPoll.objects.all()
    serializer_class = CompletedPollSerializer

    @action(detail=False, permission_classes=[IsAuthenticated])
    def get_user_history(self, request):
        completed_polls = CompletedPoll.objects.filter(user_id=request.user.id).order_by('poll')
        serializer = CompletedPollDetailSerializer(completed_polls, many=True)
        return Response(serializer.data)

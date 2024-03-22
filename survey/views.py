from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView

from survey.models import Question, SurveyResult
from survey.serializers import QuestionSerializer, SurveyResultSerializer


class QuestionsAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyResultCreateAPIView(CreateAPIView):
    serializer_class = SurveyResultSerializer
    queryset = SurveyResult.objects.all()



class AnalyticsAPIView(ListAPIView):
    queryset = SurveyResult.objects.all()
    serializer_class = SurveyResultSerializer
    permission_classes = [permissions.IsAdminUser]

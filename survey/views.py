from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from survey.models import Question, SurveyResult
from survey.serializers import QuestionSerializer


class QuestionsAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyResultCreateAPIView(CreateAPIView):
    queryset = None
    serializer_class = None

class AnalyticsAPIView(ListAPIView):
    queryset = SurveyResult
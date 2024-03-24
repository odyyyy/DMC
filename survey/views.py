from django.db.models import Avg
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from survey.models import Question, SurveyUserResult
from survey.serializers import QuestionSerializer, SurveyResultSerializer, AnalyticsSerializer, \
    AnalyticsQuestionSerializer
from survey.services import get_filtered_queryset_by_date


class QuestionsAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyResultCreateAPIView(CreateAPIView):
    serializer_class = SurveyResultSerializer
    queryset = SurveyUserResult.objects.all()


class AnalyticsQuestionWithOverallRatingAPIView(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()

        serializer = AnalyticsQuestionSerializer(questions, many=True)

        survey_overall_avg_rating = SurveyUserResult.objects.aggregate(Avg("average_rating"))['average_rating__avg']

        data = serializer.data
        data.append({'survey_overall_avg_rating': survey_overall_avg_rating})

        return Response(data)


class AnalyticsAllSurveyResultsAPIView(ListAPIView):
    serializer_class = AnalyticsSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        date_filter_query = self.request.GET.get('q')
        if date_filter_query is not None:  # Если передан параметр делаем фильтрацию
            filtered_queryset_by_date = get_filtered_queryset_by_date(date_filter_query)
            return filtered_queryset_by_date.order_by('-published_datetime')
        else:
            return SurveyUserResult.objects.all()


class AnalyticsAPIView(ListAPIView):
    queryset = SurveyUserResult.objects.order_by('-published_datetime')[:5]
    serializer_class = AnalyticsSerializer
    permission_classes = [permissions.IsAdminUser]

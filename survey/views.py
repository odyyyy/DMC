from typing import List

from django.db.models import Avg, QuerySet
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from survey.models import Question, SurveyUserResult, Survey
from survey.serializers import QuestionSerializer, SurveyResultSerializer, AnalyticsSerializer, \
    AnalyticsQuestionSerializer
from survey.services import get_filtered_survey_result_queryset_by_date, is_valid_date_filter_query, \
    get_questions_with_filtered_avg_rating


class QuestionsAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyResultCreateAPIView(CreateAPIView):
    serializer_class = SurveyResultSerializer
    queryset = SurveyUserResult.objects.all()


class AnalyticsQuestionWithOverallRatingAPIView(APIView):
    def get(self, request, format=None):
        date_filter_questions_query = self.request.GET.get('q')
        if is_valid_date_filter_query(date_filter_questions_query):
            filtered_queryset_by_date = get_filtered_survey_result_queryset_by_date(date_filter_questions_query)
            questions_with_filtered_avg_rating: List = get_questions_with_filtered_avg_rating(filtered_queryset_by_date)

            return Response(questions_with_filtered_avg_rating)

        questions = Question.objects.all()

        serializer = AnalyticsQuestionSerializer(questions, many=True)

        survey_overall_avg_rating = SurveyUserResult.objects.aggregate(Avg("average_rating"))['average_rating__avg']

        survey_overall_avg_rating = round(survey_overall_avg_rating, 2)

        data = serializer.data
        data.append({'survey_overall_avg_rating': survey_overall_avg_rating})

        return Response(data)


class AnalyticsAllSurveyResultsAPIView(ListAPIView):
    serializer_class = AnalyticsSerializer

    def get_queryset(self):
        date_filter_query = self.request.GET.get('q')
        # Если передан параметр делаем фильтрацию
        if is_valid_date_filter_query(date_filter_query):
            filtered_queryset_by_date = get_filtered_survey_result_queryset_by_date(date_filter_query)
            return filtered_queryset_by_date.order_by('-published_datetime')
        else:
            return SurveyUserResult.objects.all().order_by('-published_datetime')


class AnalyticsAPIView(ListAPIView):
    queryset = SurveyUserResult.objects.order_by('-published_datetime')[:5]
    serializer_class = AnalyticsSerializer

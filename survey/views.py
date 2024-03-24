from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView

from survey.models import Question, SurveyUserResult
from survey.serializers import QuestionSerializer, SurveyResultSerializer, AnalyticsSerializer
from survey.services import get_filtered_queryset_by_date


class QuestionsAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyResultCreateAPIView(CreateAPIView):
    serializer_class = SurveyResultSerializer
    queryset = SurveyUserResult.objects.all()


class AnalyticsAllSurveyResultAPIView(ListAPIView):
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

# Business Logic
from datetime import timedelta

from django.utils import timezone

from survey.models import SurveyUserResult


def get_filtered_queryset_by_date(date_filter_query: str):
    # TODO: Нужно фильтровать за текущий месяц (номер месяца) или по продолжительности в месяц
    today = timezone.now()
    filter_options = {
        'day': today - timedelta(days=1),
        'week': today - timedelta(days=7),
        'month': today - timedelta(days=30),
        'year': today - timedelta(days=365)
    }
    filter_by = filter_options[date_filter_query]

    filtered_queryset_by_date = SurveyUserResult.objects.filter(published_datetime__gte=filter_by)
    return filtered_queryset_by_date


def is_valid_date_filter_query(date_filter_query: str):
    return date_filter_query is not None and date_filter_query in ['day', 'week', 'month', 'year']

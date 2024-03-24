# Business Logic
from datetime import timedelta

from django.utils import timezone

from survey.models import SurveyUserResult


def get_filtered_queryset_by_date(date_filter_query: str):
    # TODO: Нужно фильтровать за текущий месяц (номер месяца) или по продолжительности в месяц
    today = timezone.now()
    if date_filter_query == "day":
        filtered_queryset_by_day = SurveyUserResult.objects.filter(published_datetime=(today - timedelta(days=1)))
        return filtered_queryset_by_day

    elif date_filter_query == "week":
        # year, week, _ = now().isocalendar()
        # return SurveyUserResult.objects.filter(published_datetime__year=year,
        #                                        published_datetime__week=week)

        filtered_queryset_by_week = SurveyUserResult.objects.filter(
            published_datetime__gte=today - timedelta(days=7))
        return filtered_queryset_by_week.order_by('-published_datetime')


    elif date_filter_query == "month":
        filtered_queryset_by_month = SurveyUserResult.objects.filter(
            published_datetime__gte=today - timedelta(days=30))
        return filtered_queryset_by_month.order_by('-published_datetime')

    elif date_filter_query == "year":
        filtered_queryset_by_year = SurveyUserResult.objects.filter(
            published_datetime__gte=today - timedelta(days=365))
        return filtered_queryset_by_year.order_by('-published_datetime')
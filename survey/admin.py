from django.contrib import admin

from .models import SurveyResult, Question


class SurveyResultAdmin(admin.ModelAdmin):
    list_filter = (
        ('published_datetime', admin.DateFieldListFilter),
    )

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     return queryset
    #
    # def date_day(self, obj):
    #     return obj.published_datetime.day
    #
    # def date_week(self, obj):
    #     return obj.published_datetime.isocalendar()[1]
    #
    # def date_month(self, obj):
    #     return obj.published_datetime.month
    #
    # def date_year(self, obj):
    #     return obj.published_datetime.year

    # date_day.admin_order_field = 'date'
    # date_day.short_description = 'Day'
    #
    # date_week.admin_order_field = 'date'
    # date_week.short_description = 'Week'
    #
    # date_month.admin_order_field = 'date'
    # date_month.short_description = 'Month'
    #
    # date_year.admin_order_field = 'date'
    # date_year.short_description = 'Year'


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(SurveyResult, SurveyResultAdmin)
admin.site.register(Question, QuestionAdmin)

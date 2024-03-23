from django.contrib import admin

from .models import SurveyResult, Question


class SurveyResultAdmin(admin.ModelAdmin):
    list_filter = (
        ('published_datetime', admin.DateFieldListFilter),
    )
    list_display = ('car_number', 'average_rating','published_datetime')


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(SurveyResult, SurveyResultAdmin)
admin.site.register(Question, QuestionAdmin)

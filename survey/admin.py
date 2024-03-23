from django.contrib import admin

from .models import SurveyUserResult, Question, Survey


class SurveyUserResultAdmin(admin.ModelAdmin):
    list_filter = (
        ('published_datetime', admin.DateFieldListFilter),
    )
    list_display = ('car_number', 'average_rating', 'published_datetime')
    search_fields = ('car_number',)


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('car_number_text', 'question_text', 'rating')
    list_filter = ('question__question',)
    search_fields = ('car_number__car_number',)

    @staticmethod
    def question_text(obj):
        return obj.question.question

    @staticmethod
    def car_number_text(obj):
        return obj.car_number.car_number


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_average_rating')
    list_filter = ('question',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(SurveyUserResult, SurveyUserResultAdmin)
admin.site.register(Survey, SurveyAdmin)

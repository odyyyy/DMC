from django.contrib import admin

from .models import SurveyUserResult, Question, Survey


class SurveyUserResultAdmin(admin.ModelAdmin):
    list_filter = (
        ('published_datetime', admin.DateFieldListFilter),
    )
    list_display = ('car_number', 'average_rating','published_datetime')

class SurveyAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(SurveyUserResult, SurveyUserResultAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Survey, SurveyAdmin)

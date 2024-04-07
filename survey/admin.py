from django.contrib import admin

from .models import SurveyUserResult, Question, Survey


class SurveyUserResultAdmin(admin.ModelAdmin):
    list_filter = (
        ('published_datetime', admin.DateFieldListFilter),
    )
    list_display = ('id', 'car_number', 'average_rating', 'published_datetime')
    search_fields = ('car_number',)
    readonly_fields = ('average_rating', 'comment')


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('car_number_id', 'car_number_text', 'question', 'rating')
    list_filter = ('question',)
    search_fields = ('car_number__car_number',)
    readonly_fields = ('rating',)

    @admin.display(description="Номер автомобиля")
    def car_number_text(self, obj):
        return obj.car_number.car_number

    @admin.display(description="ID")
    def car_number_id(self, obj):
        return obj.car_number.id


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_average_rating')
    list_filter = ('question',)
    search_fields = ('question',)
    readonly_fields = ('question_average_rating',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(SurveyUserResult, SurveyUserResultAdmin)
admin.site.register(Survey, SurveyAdmin)

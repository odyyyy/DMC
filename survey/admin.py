from django.contrib import admin

from .models import SurveyResult

class SurveyResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(SurveyResult, SurveyResultAdmin)

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from survey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('feedback/rate', views.QuestionsAPIView.as_view(), name='feedback-rate'),
    path('feedback/send', views.SurveyResultCreateAPIView.as_view(), name='feedback-send'),
    path('analytics/', views.AnalyticsAPIView.as_view(), name='analytics'),
    path('analytics/all', views.AnalyticsAllSurveyResultsAPIView.as_view(), name='analytics'),
    path('analytics/questions', views.AnalyticsQuestionWithOverallRatingAPIView.as_view(), name='analytics'),

]


from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from rest_framework import serializers


from survey.models import Question, SurveyUserResult, Survey


class AnalyticsSerializer(serializers.ModelSerializer):
    published_datetime = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = SurveyUserResult
        fields = ['car_number', 'average_rating', 'published_datetime']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question', ]


class AnalyticsQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SurveyResultSerializer(serializers.ModelSerializer):
    questions_answers = serializers.JSONField(write_only=True)

    class Meta:
        model = SurveyUserResult
        fields = ['car_number', 'questions_answers', 'average_rating', 'comment']

    def create(self, validated_data):
        """ Создание записи о отзыве и обновление среднего рейтинга вопросов """
        car_number = validated_data.get('car_number')
        survey_result = SurveyUserResult(
            car_number=car_number,
            average_rating=validated_data.get('average_rating'),
            comment=validated_data.get('comment')
        )

        survey_result.save()

        for question, rating in validated_data['questions_answers'].items():
            question_queryset = Question.objects.filter(question=question)
            if question_queryset.exists():
                # Добавляем все вопросы и оценки пользователя
                Survey.objects.create(car_number=survey_result, question=question, rating=rating)

                # Пересчитываем среднюю оценку для каждого вопроса
                new_avg_rating = Survey.objects.filter(question=question).aggregate(Avg("rating"))['rating__avg']

                question_queryset.update(question_average_rating=new_avg_rating)
            else:
                raise ObjectDoesNotExist("Вопрос не найден в базе данных!")

        return survey_result

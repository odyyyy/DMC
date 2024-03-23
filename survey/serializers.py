from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import F
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from survey.models import Question, SurveyResult


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class SurveyResultSerializer(serializers.Serializer):
    car_number = serializers.CharField(max_length=10)
    questions_answers = serializers.JSONField()
    average_rating = serializers.DecimalField(max_digits=2, decimal_places=1,
                                              validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = serializers.CharField(allow_blank=True)

    def create(self, validated_data):
        """ Создание записи о отзыве и обновление среднего рейтинга вопросов """

        survey_result = SurveyResult(
            car_number=validated_data.get('car_number'),
            questions_answers=validated_data.get('questions_answers'),
            average_rating=validated_data.get('average_rating'),
            comment=validated_data.get('comment')
        )
        for question, answer in validated_data['questions_answers'].items():
            question_object = Question.objects.filter(question=question)
            if question_object.exists() and question_object[0].average_rating != 0:
                question_object.update(count=F("count") + 1)
                question_object.update(average_rating=(int(question_object[0].average_rating) + 1 + answer) / question_object[0].count)

            elif question_object.exists() and question_object[0].average_rating == 0:
                question_object.update(count=F("count") + 1)
                question_object.update(average_rating=answer)

        survey_result.save()
        return survey_result

    def validate_answers(self, value):
        for rating in value.values():
            if rating not in [1, 2, 3, 4, 5]:
                raise serializers.ValidationError("Рейтинг должен быть значением от 1 до 5.")
        return value

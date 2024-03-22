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
    average_rating = serializers.DecimalField(max_digits=2, decimal_places=1)
    comment = serializers.CharField(allow_blank=True)

    def create(self, validated_data):

        survey_result = SurveyResult(
            car_number=validated_data.get('car_number'),
            questions_answers=validated_data.get('questions_answers'),
            average_rating=validated_data.get('average_rating'),
            comment=validated_data.get('comment')
        )

        for question, answer in validated_data['questions_answers'].items():
            question_object = get_object_or_404(Question, question=question)
            if question_object.average_rating != 0:
                question_object.average_rating = (F("average_rating") + answer) / 2
            else:
                question_object.average_rating = answer
            question_object.save()

        survey_result.save()
        return survey_result

    def validate_answers(self,value):
        for rating in value.values():
            if rating not in [1, 2, 3, 4, 5]:
                raise serializers.ValidationError("Рейтинг должен быть значением от 1 до 5.")
        return value



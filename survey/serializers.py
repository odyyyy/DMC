from rest_framework import serializers

from survey.models import Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"


class SurveyResultSerializer(serializers.Serializer):
    car_number = serializers.CharField(max_length=20)
    answers = serializers.DictField()
    comment = serializers.CharField(allow_blank=True)

    def validate_answers(self, value):
        for rating in value.values():
            if rating not in [1, 2, 3, 4, 5]:
                raise serializers.ValidationError("Рейтинг должен быть значением от 1 до 5.")
        return value
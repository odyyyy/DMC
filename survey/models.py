from django.db import models
from django.utils import timezone


class Question(models.Model):
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    average_rating = models.DecimalField(decimal_places=1, max_digits=2, default=0, verbose_name="Средняя оценка")

    def __str__(self):
        return f"{self.question} - {self.average_rating}"

    class Meta:
        verbose_name = "Вопросы"
        verbose_name_plural = "Вопросы"
        ordering = ["id"]


class SurveyResult(models.Model):
    car_number = models.CharField(max_length=10, unique=True, db_index=True, verbose_name="Номер автомобиля")
    questions_answers = models.JSONField(verbose_name="Вопросы и ответы")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    average_rating = models.DecimalField(decimal_places=1, max_digits=2, verbose_name="Средняя оценка")
    published_datetime = models.DateTimeField(default=timezone.now, verbose_name="Дата и время")

    class Meta:
        verbose_name = "Результаты опросов"
        verbose_name_plural = "Результаты опросов"
        ordering = ["id"]

    def __str__(self):
        return f"Номер: {self.car_number} - Ср. Оценка: {self.average_rating}"

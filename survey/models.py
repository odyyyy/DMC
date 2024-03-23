from decimal import Decimal, ROUND_DOWN

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """ Таблица со всеми вопросами и их ср. рейтингом """
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0,
                                         verbose_name="Средняя оценка")

    def __str__(self):
        return f"{self.question} --- {self.average_rating}"

    class Meta:
        verbose_name = "Вопросы"
        verbose_name_plural = "Вопросы"
        ordering = ["id"]


class SurveyUserResult(models.Model):
    """ Таблица с информацией о результатах прохождения опроса пользователем """
    car_number = models.CharField(max_length=10, unique=True, db_index=True, verbose_name="Номер автомобиля")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Средняя оценка")
    published_datetime = models.DateTimeField(default=timezone.now, verbose_name="Дата и время")

    class Meta:
        verbose_name = "Результаты опросов"
        verbose_name_plural = "Результаты опросов"
        ordering = ["id"]

    def __str__(self):
        return f"Номер: {self.car_number} --- Ср. Оценка: {self.average_rating}"


class Survey(models.Model):
    car_number = models.ForeignKey(SurveyUserResult, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])

    class Meta:
        verbose_name = "Оценки пользователей"
        verbose_name_plural = "Оценки пользователей"
        ordering = ["id"]
        unique_together = ('car_number', 'question')

    def __str__(self):
        return f"{self.car_number} --- {self.question} --- {self.rating}"
# Generated by Django 5.0.3 on 2024-03-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_question_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='average_rating',
            field=models.FloatField(default=0, verbose_name='Средняя оценка'),
        ),
    ]
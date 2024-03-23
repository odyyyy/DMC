# Generated by Django 5.0.3 on 2024-03-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_alter_question_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresult',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Средняя оценка'),
        ),
    ]

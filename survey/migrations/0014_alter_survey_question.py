# Generated by Django 5.0.3 on 2024-03-23 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0013_alter_survey_options_remove_question_average_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.question'),
        ),
    ]
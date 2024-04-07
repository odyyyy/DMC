# Business Logic
from datetime import timedelta

from django.utils import timezone

from survey.models import SurveyUserResult, Survey, Question


def get_questions_with_filtered_avg_rating(filtered_queryset_by_date):
    ratings_for_all_questions = {}

    for result in filtered_queryset_by_date:
        answers = Survey.objects.filter(car_number_id=result.id)

        for answer in answers:
            question = answer.question
            # Если нет вопроса в бд то скипаем
            if not (Question.objects.filter(question=question).exists()):
                continue

            rating = answer.rating
            if question in ratings_for_all_questions:
                ratings_for_all_questions[question].append(rating)
            else:
                ratings_for_all_questions[question] = [rating]

    question_avg_ratings = []
    element_id = 0
    for question, ratings in ratings_for_all_questions.items():
        avg_rating = round(sum(ratings) / len(ratings), 2)
        question_avg_ratings.append({
            'id': element_id,
            'question': question,
            "question_average_rating": avg_rating
        })
        element_id += 1

    return question_avg_ratings


def get_filtered_survey_result_queryset_by_date(date_filter_query: str):
    today = timezone.now()
    filter_options = {
        'day': today - timedelta(days=1),
        'week': today - timedelta(days=7),
        'month': today - timedelta(days=30),
        'year': today - timedelta(days=365)
    }
    filter_by = filter_options[date_filter_query]

    filtered_queryset_by_date = SurveyUserResult.objects.filter(published_datetime__gte=filter_by)
    return filtered_queryset_by_date


def is_valid_date_filter_query(date_filter_query: str):
    return date_filter_query is not None and date_filter_query in ['day', 'week', 'month', 'year']

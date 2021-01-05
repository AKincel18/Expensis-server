from django.db.models import Avg

from commons.service import get_all_income_ranges, get_all_age_ranges, full_gender_name, range_to_string
from expenses.models import Expense
from stats.services.common_stats_service import get_value_from_filtering, get_average_expenses_by_params, \
    get_age_range_id_by_user_birth_date
from stats.stats_class import StatsResponse


def separated_stat(filters, user):
    user_avg_filter = Expense.objects.filter(user=user).aggregate(Avg('value'))
    user_avg = round(get_value_from_filtering(user_avg_filter.get('value__avg')), 2)
    if filters.income_range:
        return income_range_separated_stat(user.income_range.id, user_avg)
    elif filters.age_range:
        return age_range_separated_stat(user.birth_date, user_avg)
    elif filters.gender:
        return gender_separated_stat(user.gender, user_avg)


def income_range_separated_stat(user_income_range_id, user_avg):
    income_ranges = get_all_income_ranges()
    response = list()
    for income_range in income_ranges:
        income_range_id = income_range['id']
        income_range_string = range_to_string(income_range)
        all_avg = get_average_expenses_by_params('income_range', income_range_id)
        if income_range_id == user_income_range_id:
            response.append(StatsResponse(income_range_string, user_avg, all_avg))
        else:
            response.append(StatsResponse(income_range_string, 0.0, all_avg))
    return response


def age_range_separated_stat(user_birth_date, user_avg):
    age_ranges = get_all_age_ranges()
    user_age_range_id = get_age_range_id_by_user_birth_date(user_birth_date)
    response = list()
    for age_range in age_ranges:
        age_range_id = age_range['id']
        age_range_string = range_to_string(age_range)
        all_avg = get_average_expenses_by_params('age_range', age_range_id)
        if age_range_id == user_age_range_id:
            response.append(StatsResponse(age_range_string, user_avg, all_avg))
        else:
            response.append(StatsResponse(age_range_string, 0.0, all_avg))
    return response


def gender_separated_stat(user_gender, user_avg):
    response = list()
    for gender in ['F', 'M']:
        full_gender = full_gender_name(gender)
        all_avg = get_average_expenses_by_params('gender', gender)
        if gender == user_gender:
            response.append(StatsResponse(full_gender, user_avg, all_avg))
        else:
            response.append(StatsResponse(full_gender, 0.0, all_avg))
    return response

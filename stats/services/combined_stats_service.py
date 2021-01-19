from django.db.models import Avg

from commons.service import age_range_to_string, full_gender_name
from expenses.models import Expense
from stats.services.common_stats_service import get_age_range_id_by_user_birth_date, get_value_from_filtering, \
    get_average_expenses_by_params
from stats.stats_class import StatsResponse


def combined_stats(filters, user):
    user_avg_filter = Expense.objects.filter(user=user).aggregate(Avg('value'))
    user_avg = round(get_value_from_filtering(user_avg_filter.get('value__avg')), 2)
    response = list()

    if filters.income_range:
        income_range_avg = get_average_expenses_by_params('income_range', user.income_range)
        response.append(StatsResponse('Income range: ' + str(user.income_range),
                                      user_avg, income_range_avg))
    if filters.age_range:
        user_age_range_id = get_age_range_id_by_user_birth_date(user.birth_date)
        age_range_avg = get_average_expenses_by_params('age_range', user_age_range_id)
        user_age_range_string = age_range_to_string(user_age_range_id)
        response.append(StatsResponse('Age range: ' + user_age_range_string,
                                      user_avg, age_range_avg))
    if filters.gender:
        gender_avg = get_average_expenses_by_params('gender', user.gender)
        gender_string = full_gender_name(user.gender)
        response.append(StatsResponse('Gender: ' + gender_string,
                                      user_avg, gender_avg))
    return response


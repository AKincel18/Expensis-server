from django.db.models import Avg, Sum

from commons.service import age_range_to_string, full_gender_name
from expenses.models import Expense
from stats.models import Stat
from stats.services.common_stats_service import get_age_range_id_by_user_birth_date, get_value_from_filtering
from stats.stats_class import StatsResponse


def combined_stat(filters, user):
    user_avg_filter = Expense.objects.filter(user=user).aggregate(Avg('value'))
    user_avg = get_value_from_filtering(user_avg_filter.get('value__avg'))
    response = list()

    if filters.income_range:
        income_range_avg = get_average_expenses_by_params('income_range', user.income_range)
        response.append(StatsResponse('Income range: ' + str(user.income_range),
                                      round(user_avg, 2), round(income_range_avg, 2)))
    if filters.age_range:
        user_age_range_id = get_age_range_id_by_user_birth_date(user.birth_date)
        age_range_avg = get_average_expenses_by_params('age_range', user_age_range_id)
        user_age_range_string = age_range_to_string(user_age_range_id)
        response.append(StatsResponse('Age range: ' + user_age_range_string,
                                      round(user_avg, 2), round(age_range_avg, 2)))
    if filters.gender:
        gender_avg = get_average_expenses_by_params('gender', user.gender)
        gender_string = full_gender_name(user.gender)
        response.append(StatsResponse('Gender: ' + gender_string,
                                      round(user_avg, 2), round(gender_avg, 2)))
    return response


def get_average_expenses_by_params(filter_name, filter_value):
    my_filter = {filter_name: filter_value}
    sum_value_filter = Stat.objects.filter(**my_filter).aggregate(Sum('value'))
    sum_value = get_value_from_filtering(sum_value_filter.get('value__sum'))
    count_value_filter = Stat.objects.filter(**my_filter).aggregate(Sum('count'))
    count_value = get_value_from_filtering(count_value_filter.get('count__sum'))
    if count_value != 0:
        return float(sum_value) / float(count_value)
    return 0.0

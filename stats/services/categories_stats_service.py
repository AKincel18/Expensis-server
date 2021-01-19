from django.db.models import Sum, Avg

from commons.models import Category
from expenses.models import Expense
from stats.models import Stats
from stats.services.common_stats_service import get_age_range_id_by_user_birth_date, get_value_from_filtering
from stats.stats_class import StatsResponse


def categories_stats(filters, user):
    filtered_stats = filter_stats(user, filters)
    return get_average_categories_stats(user, filtered_stats)


def get_average_categories_stats(user, filtered_stats):
    categories = Category.objects.all()
    response = list()
    for category in categories:
        user_average = get_expenses_average_value_by_user_and_category(user, category)
        all_average = get_all_expenses_average_value_by_and_category(category, filtered_stats)
        response.append(StatsResponse(category.value, round(user_average, 2), round(all_average, 2)))
    return response


def filter_stats(user, filters):
    stats = Stats.objects.all()
    if filters.income_range:
        stats = stats.filter(income_range=user.income_range)
    if filters.age_range:
        user_age_range = get_age_range_id_by_user_birth_date(user.birth_date)
        stats = stats.filter(age_range=user_age_range)
    if filters.gender:
        stats = stats.filter(gender=user.gender)
    return stats


def get_all_expenses_value_by_category(category, filtered_stats):
    all_value_filter = filtered_stats.filter(category=category).aggregate(Sum('value'))
    return get_value_from_filtering(all_value_filter.get('value__sum'))


def get_expenses_average_value_by_user_and_category(user, category):
    user_value_filter = Expense.objects.filter(category=category, user=user).aggregate(Avg('value'))
    return get_value_from_filtering(user_value_filter.get('value__avg'))


def get_all_expenses_average_value_by_and_category(category, filtered_stats):
    sum_value = get_all_expenses_value_by_category(category, filtered_stats)
    count_value_filter = filtered_stats.filter(category=category).aggregate(Sum('count'))
    count_value = get_value_from_filtering(count_value_filter.get('count__sum'))
    if count_value != 0:
        return float(sum_value) / float(count_value)
    else:
        return 0.0

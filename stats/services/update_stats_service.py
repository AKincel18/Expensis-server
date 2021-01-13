from decimal import Decimal

from stats.models import Stat
from stats.services.common_stats_service import get_age_range_id_by_user_birth_date
from stats.stats_class import ExpenseAction
from users.service import get_user_by_id

"""
updating stats table after an expense was created or updated
"""


def update_stats_create_update(serializer, action, *args):
    user = get_user_by_id(serializer.validated_data['user'].id)
    category_id = serializer.data["category"]
    age_range_id = get_age_range_id_by_user_birth_date(user.birth_date)
    value = Decimal(serializer.data["value"])

    stat = Stat.objects.filter(
        income_range=user.income_range,
        age_range=age_range_id,
        category=category_id,
        gender=user.gender
    ).first()
    if action == ExpenseAction.CREATE:
        stat.value += value
        stat.count += 1
    elif action == ExpenseAction.UPDATE:
        stat.value -= args[0]  # subtract the old value
        stat.value += value  # add the new value
    Stat.save(stat)


"""
updating stats table after an expense was deleted
"""


def update_stats_delete(expense):
    age_range_id = get_age_range_id_by_user_birth_date(expense.user.birth_date)
    value = Decimal(expense.value)
    stat = Stat.objects.filter(
        income_range=expense.user.income_range,
        age_range=age_range_id,
        category=expense.category.id,
        gender=expense.user.gender
    ).first()

    stat.value -= value
    stat.count -= 1
    Stat.save(stat)

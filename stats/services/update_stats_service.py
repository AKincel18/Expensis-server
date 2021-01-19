from decimal import Decimal

from stats.models import Stats
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

    if action == ExpenseAction.CREATE:
        stats = get_stats(user.income_range, age_range_id, category_id, user.gender)
        stats.value += value
        stats.count += 1
        Stats.save(stats)

    elif action == ExpenseAction.UPDATE:
        old_value = args[0]
        old_category_id = args[1]
        if category_id == old_category_id:
            stats = get_stats(user.income_range, age_range_id, category_id, user.gender)
            stats.value -= old_value  # subtract the old value
            stats.value += value  # add the new value
            Stats.save(stats)
        else:
            stats1 = get_stats(user.income_range, age_range_id, category_id, user.gender)
            stats1.value += value
            stats1.count += 1
            Stats.save(stats1)

            stats2 = get_stats(user.income_range, age_range_id, old_category_id, user.gender)
            stats2.value -= old_value
            stats2.count -= 1
            Stats.save(stats2)


"""
updating stats table after an expense was deleted
"""


def update_stats_delete(expense):
    age_range_id = get_age_range_id_by_user_birth_date(expense.user.birth_date)
    value = Decimal(expense.value)
    stats = get_stats(expense.user.income_range, age_range_id, expense.category_id, expense.user.gender)
    stats.value -= value
    stats.count -= 1
    Stats.save(stats)


def get_stats(income_range, age_range_id, category_id, gender):
    return Stats.objects.filter(
        income_range=income_range,
        age_range=age_range_id,
        category=category_id,
        gender=gender
    ).first()

import random
from decimal import Decimal

from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response

from commons.models import Category
from expenses.models import Expense
from stats.models import Stat
from stats.services.common_stats_service import get_age_range_id_by_user_birth_date
from users.service import get_user_by_id

"""
to generate expenses (and update stats), please add code:
return generate_expenses_testing()
in a post method in an ExpenseList
"""


def generate_expenses_testing():
    for i in range(1, 10000):
        user_id = random.randint(1, 10)
        user = get_user_by_id(user_id)
        category_id = random.randint(1, 3)
        category = Category.objects.get(id=category_id)
        value = random.randint(1, 10000)
        expense = Expense(
            user=user,
            date=timezone.now(),
            title='test title',
            description='test desc',
            category=category,
            value=value
        )
        Expense.save(expense)
        update_stats_testing(expense)
    return Response(status=status.HTTP_201_CREATED)


def update_stats_testing(expense):
    age_range_id = get_age_range_id_by_user_birth_date(expense.user.birth_date)
    value = Decimal(expense.value)
    stat = Stat.objects.filter(
        income_range=expense.user.income_range,
        age_range=age_range_id,
        category=expense.category.id,
        gender=expense.user.gender
    ).first()

    stat.value += value
    stat.count += 1
    Stat.save(stat)

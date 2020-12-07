from expenses.models import Expense


def get_expense_by_id(expense_id):
    try:
        return Expense.objects.get(id=expense_id)
    except Expense.DoesNotExist:
        return None

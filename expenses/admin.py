from django.contrib import admin
from expenses.models import Expense

admin.site.register(Expense)


class ExpenseInline(admin.TabularInline):
    model = Expense

from django.contrib import admin

from commons.models import IncomeRange, AgeRange, Category
from expenses.admin import ExpenseInline
from users.admin import UserInline

admin.site.register(AgeRange)


@admin.register(IncomeRange)
class IncomeRangeAdmin(admin.ModelAdmin):
    inlines = [
        UserInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ExpenseInline
    ]
from django.contrib import admin

from commons.models import IncomeRange, AgeRange, Category
from users.admin import UserInline

admin.site.register(AgeRange)
admin.site.register(Category)


@admin.register(IncomeRange)
class IncomeRangeAdmin(admin.ModelAdmin):
    inlines = [
        UserInline,
    ]

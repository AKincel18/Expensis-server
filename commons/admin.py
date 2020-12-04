from django.contrib import admin
from users.admin import UserInline
from commons.models import IncomeRanges, AgeRanges, Categories

# Register your models here.

admin.site.register(AgeRanges)
admin.site.register(Categories)


@admin.register(IncomeRanges)
class IncomeRangesAdmin(admin.ModelAdmin):
    inlines = [
        UserInline,
    ]

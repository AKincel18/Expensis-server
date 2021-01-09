import datetime

from django.db import models
from django.db.models import CASCADE

from commons.models import Category
from users.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses', on_delete=CASCADE)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=150, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    value = models.DecimalField(decimal_places=2, max_digits=19)

    def __str__(self):
        return self.title

from django.db import models
from rest_framework.validators import UniqueValidator


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    gender = models.CharField(max_length=1)  # 'F' -> female, 'M' -> male
    birth_date = models.DateField()
    monthly_limit = models.FloatField()
    income_scope = models.ForeignKey(
        'commons.IncomeRanges',
        on_delete=models.SET_NULL,
        null=True
    )

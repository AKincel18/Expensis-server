from django.db import models


class Stat(models.Model):
    income_range = models.ForeignKey('commons.IncomeRange', on_delete=models.SET_NULL, null=True)
    age_range = models.ForeignKey('commons.AgeRange', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('commons.Category', on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=1)  # 'F' -> female, 'M' -> male
    value = models.DecimalField(decimal_places=2, max_digits=19)
    count = models.IntegerField()

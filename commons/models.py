from django.db import models


# Create your models here.
class IncomeRanges(models.Model):
    range_from = models.IntegerField()
    range_to = models.IntegerField()


class AgeRanges(models.Model):
    range_from = models.IntegerField()
    range_to = models.IntegerField()


class Categories(models.Model):
    value = models.CharField(max_length=50)

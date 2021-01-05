from django.db import models


class IncomeRange(models.Model):
    range_from = models.IntegerField()
    range_to = models.IntegerField()

    def __str__(self):
        return str(self.range_from) + " - " + str(self.range_to)


class AgeRange(models.Model):
    range_from = models.IntegerField()
    range_to = models.IntegerField()


class Category(models.Model):
    value = models.CharField(max_length=50)

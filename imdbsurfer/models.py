from django.db import models

from common.models import CommonInfo 


class Movie(CommonInfo):
    year = models.PositiveSmallIntegerField()
    index = models.PositiveSmallIntegerField()
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    votes = models.PositiveIntegerField()
    link = models.CharField(max_length=255)
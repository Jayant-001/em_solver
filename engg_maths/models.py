from django.db import models
from django.db.models.base import Model

# Create your models here.

class MathData(models.Model) :
    x_list = models.CharField(max_length=100)
    y_list = models.CharField(max_length=100)
    x2_list = models.CharField(max_length=100)
    xy_list = models.CharField(max_length=100)


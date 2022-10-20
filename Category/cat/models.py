from django.db import models


class Cat(models.Model):
    catName = models.CharField(max_length=200)
    catDesc = models.CharField(max_length=200)

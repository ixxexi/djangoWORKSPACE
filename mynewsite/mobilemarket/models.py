# _*_ coding: utf-8 _*_
from django.db import models


# Create your models here.
class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.SET_DEFAULT, default=2)
    name = models.CharField(max_length=20)
    url = models.URLField(default="http://mis.com")

    def __str__(self):
        return self.name


class Product(models.Model):
    pmodel = models.ForeignKey(
        PModel, on_delete=models.SET_DEFAULT, default=4, verbose_name="型號"
    )
    nickname = models.CharField(max_length=15, default="超值二手機")
    description = models.TextField(default="暫無說明")
    year = models.PositiveIntegerField(default=2016)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname


class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default="產品照片")
    url = models.URLField(default="http://mis.com")

    def __str__(self):
        return self.description

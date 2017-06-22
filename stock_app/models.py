from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=150)


class Stock(models.Model):
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=5, unique=True)
    price = models.IntegerField
    price_target = models.IntegerField
    is_bullish = models.BooleanField

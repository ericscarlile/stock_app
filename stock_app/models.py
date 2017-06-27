from django.db import models

# Create your models here.


class Stock(models.Model):
    name = models.CharField(max_length=50)
    ticker = models.CharField(max_length=5, unique=True)
    price = models.FloatField(null=True)
    price_target = models.FloatField(null=True)
    is_bullish = models.NullBooleanField(null=True)
    last_updated = models.DateField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=24, unique=True)
    password = models.CharField(max_length=150)
    stocks = models.ManyToManyField(Stock)

    def __str__(self):
        return self.username

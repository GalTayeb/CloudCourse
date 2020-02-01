from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    availableItems = models.IntegerField()


class Order(models.Model):
    date = models.DateTimeField()
    listOfProducts = models.ManyToManyField(Product)
    status = models.BooleanField(default=False)

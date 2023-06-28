from django.db import models

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True)


class Driver(models.Model):
    name = models.CharField(max_length=255)
    cars = models.ManyToManyField(Car)



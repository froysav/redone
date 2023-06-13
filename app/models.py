from django.db import models
from modeltranslation.translator import translator, TranslationOptions


class Home(models.Model):
    picture = models.ImageField(upload_to='homes/')
    rental_period = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    taking_time = models.CharField(max_length=10)
    sqft = models.IntegerField()
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    upload_time = models.IntegerField()

    def __str__(self):
        return self.name


class Happys(models.Model):
    description = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='homese/')
    name = models.CharField(max_length=100)
    jobs = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cities(models.Model):
    picture = models.ImageField()
    place = models.CharField(max_length=100)
    properties = models.IntegerField()

    def __str__(self):
        return self.picture


class Agent(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=100)
    listing = models.CharField(max_length=100)
    properties = models.IntegerField()

    def __str__(self):
        return self.picture


class Blog(models.Model):
    picture = models.ImageField()
    date = models.DateField()
    name = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.name

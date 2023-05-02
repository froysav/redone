from django.db import models


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
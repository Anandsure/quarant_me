from django.db import models

# Create your models here.
class LocationLoggerModel(models.Model):
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=30)
    AQI = models.IntegerField()
    wuranwu = models.CharField(max_length=30)
    PM25 = models.IntegerField()
    unit = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    updated_time = models.DateTimeField()
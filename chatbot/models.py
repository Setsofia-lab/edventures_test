from django.db import models

class EconomicIndicator(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    value = models.FloatField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.country} - {self.year})"


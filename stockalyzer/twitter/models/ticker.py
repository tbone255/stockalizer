from django.db import models


class Ticker(models.Model):
    symbol = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    
    
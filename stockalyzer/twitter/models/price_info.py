from django.db import models 

class PriceInfo(models.Model):
    yesterclose = models.DecimalField(max_digits = 19, decimal_places = 2)
    first_mention = models.DecimalField(max_digits = 19, decimal_places = 2)
    last_price = models.DecimalField(max_digits = 19, decimal_places = 2)
    last_volume = models.IntegerField()

from django.db import models
from .ticker import Ticker
from .price_info import PriceInfo

class Trend(models.Model):
    ticker_id = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    count = models.IntegerField()
    priceinfo_id = models.ForeignKey(PriceInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

from django.db import models
from ./ticker import Ticker
#from ./price_info import PriceInfo

class Trend(models.Model):
    ticker_id = models.ForeignKey(Tickers)
    count = models.IntegerField()
    #priceinfo_id = models.ForeignKey(PriceInfo)
    date = models.DateField(auto_now_add=True)

from django.db import models
from ./news import News
from ./trends import Trend

class NewsTrends(models.Model):
    trends_id = models.ForeignKey(Trend)
    news_id = models.ForeignKey(News)
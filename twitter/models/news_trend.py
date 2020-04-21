from django.db import models
from .news import News
from .trends import Trend

class NewsTrend(models.Model):
    trends_id = models.ForeignKey(Trend, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)

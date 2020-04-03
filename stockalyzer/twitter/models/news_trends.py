from django.db import models
from ./news import News
from ./trends import Trend

class News_Trends(models.Model):
    trends_id = models.ForeignKey(Trend)
    news_id = models.ForeignKey(News)
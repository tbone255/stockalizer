from django.contrib import admin
from .models import *

admin.site.register(News)
admin.site.register(NewsTrend)
admin.site.register(PriceInfo)
admin.site.register(Ticker)
admin.site.register(Trend)
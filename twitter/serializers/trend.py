from rest_framework import serializers 
from ..models import Trend

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ['id', 'ticker_id', 'count', 'priceinfo_id', 'date']

class BasicTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ['id', 'count', 'date']

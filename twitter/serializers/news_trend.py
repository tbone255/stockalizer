from rest_framework import serializers 
from ..models import NewsTrend
from .news import BasicNewsSerializer
from .trend import BasicTrendSerializer

class NewsTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTrend
        fields = ['id', 'trends_id', 'news_id']

class FullNewsTrendSerializer(serializers.Serializer):
    trend = BasicTrendSerializer(source='trends_id')
    news = BasicNewsSerializer(source='news_id')

from rest_framework import serializers 
from ..models import NewsTrend

class NewsTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTrend
        fields = ['id', 'trends_id', 'news_id']

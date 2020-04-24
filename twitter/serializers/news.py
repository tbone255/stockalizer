from rest_framework import serializers 
from ..models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'url', 'title']

class BasicNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['url', 'title']

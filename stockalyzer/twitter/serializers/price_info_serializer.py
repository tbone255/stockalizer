from rest_framework import serializers 
from ..models import PriceInfo

class PriceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceInfo
        fields = ['id', 'yesterclose', 'first_mention', 'last_price', 'last_volume']
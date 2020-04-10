from rest_framework import viewsets
from ..models import PriceInfo
from ..serializers import PriceInfoSerializer

class PriceInfoViewSet(viewsets.ModelViewSet):
    queryset = PriceInfo.objects.all()
    serializer_class = PriceInfoSerializer
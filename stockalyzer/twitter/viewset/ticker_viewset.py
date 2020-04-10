from rest_framework import viewsets
from ..models import Ticker
from ..serializers import TickerSerializer

class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
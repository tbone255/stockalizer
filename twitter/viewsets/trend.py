from rest_framework import viewsets

from ..models import Trend
from ..serializers import TrendSerializer


class TrendViewSet(viewsets.ModelViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer

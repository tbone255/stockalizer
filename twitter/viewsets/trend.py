from datetime import date
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Trend
from ..serializers import TrendSerializer


class TrendViewSet(viewsets.ModelViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer

    @action(detail=False, methods=['get'])
    def top(self, request):
        yesterday = date.today()
        #yesterday = yesterday.replace(day=yesterday.day-1)
        trends = Trend.objects.filter(date=yesterday).order_by('-count')[:5]
        serializer = TrendSerializer(trends, many=True)
        return Response(serializer.data)

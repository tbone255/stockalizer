from rest_framework import filters, viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Ticker, NewsTrend
from ..serializers import TickerSerializer, FullNewsTrendSerializer


class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['symbol']

    @action(detail=True, methods=['get'])
    def trends(self, request, pk=None):
        ticker = self.get_object()
        trends = NewsTrend.objects.filter(trends_id__ticker_id=ticker.id)

        serializer = FullNewsTrendSerializer(trends, many=True)
        return Response(serializer.data)

        

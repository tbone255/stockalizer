from rest_framework import filters, viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import NewsTrend, Ticker, Trend
from ..serializers import NewsTrendNewsSerializer, BasicTrendSerializer, TickerSerializer


class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['symbol']

    @action(detail=True, methods=['get'])
    def trends(self, request, pk=None):
        ticker = self.get_object()
        trends = Trend.objects.filter(ticker_id=ticker.id)
        data = []
        for trend in trends:
            news = NewsTrend.objects.filter(trends_id=trend.id)
            news_serializer = NewsTrendNewsSerializer(news, many=True)
            final = BasicTrendSerializer(trend).data
            final['news'] = news_serializer.data
            data.append(final)

        return Response(data)

        

from iexfinance.stocks import Stock
import os
from rest_framework import filters, viewsets 
from rest_framework.decorators import action
from rest_framework.response import Response
import yfinance

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

        
    @action(detail=True, methods=['get'])
    def price_info(self, request, pk=None):
        stock = Stock(self.get_object().symbol, token=os.getenv('IEX_TOKEN'))
        return Response(stock.get_key_stats())
    
    #helper function for graph data
    def generate_technical_indicators(self, data):
         #Technical Indicators: Moving Average
        data["MA_5"] = data["Close"].rolling(window = 5).mean()
        data["MA_15"] = data["Close"].rolling(window = 15).mean()
        
        #Technical Indicators: VWAP
        data["VWAP"] = (data["Volume"]*(data["High"]+data["Low"])/2).cumsum() / data["Volume"].cumsum()
        
        #Tecnical Indicators: Bollinger Bands
        data["BB_U"] = data["MA_15"] + (data['MA_15'].rolling(15).std()*2)
        data["BB_L"] = data["MA_15"] - (data['MA_15'].rolling(15).std()*2)
        data["BB_M"] = data["MA_15"]
        data = data.dropna()       
        return data
    
    @action(detail=True, methods=['get'])
    def graph_data(self, request, pk=None):
        symbol = self.get_object().symbol
        ticker = yfinance.Ticker(symbol)
        data = ticker.history('ytd')
        data = data.reset_index()
        data["Date"] = data['Date'].dt.date
        data['Date'] = data['Date'].astype('str')
        data = generate_technical_indicators(data)
        data = data.to_dict()
        return Response(data)

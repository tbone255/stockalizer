from ..models import News
from ..serializers import NewsSerializer
from rest_framework import viewsets 

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
from ..models import NewsTrend
from ..serializers import NewsTrendSerializer
from rest_framework import viewsets 

class NewsTrendViewSet(viewsets.ModelViewSet):
    queryset = NewsTrend.objects.all()
    serializer_class = NewsTrendSerializer
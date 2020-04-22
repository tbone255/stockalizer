from rest_framework import viewsets 

from ..models import NewsTrend
from ..serializers import NewsTrendSerializer


class NewsTrendViewSet(viewsets.ModelViewSet):
    queryset = NewsTrend.objects.all()
    serializer_class = NewsTrendSerializer

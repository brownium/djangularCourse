from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import ListSerializer, QuoteSerializer
from .models import List, Quote

class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    #permission_classes = (permissions.IsAuthenticated,)


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    #permission_classes = (permissions.IsAuthenticated,)

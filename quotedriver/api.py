from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import AuthorSerializer, QuoteSerializer
from .models import Author, Quote

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    #permission_classes = (permissions.IsAuthenticated,)


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    #permission_classes = (permissions.IsAuthenticated,)

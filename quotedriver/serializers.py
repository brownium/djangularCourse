from rest_framework import serializers

from .models import List, Quote

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote

class ListSerializer(serializers.ModelSerializer):
    quotes = QuoteSerializer(read_only=True, many=True)

    class Meta:
        model = List

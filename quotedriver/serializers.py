from rest_framework import serializers

from .models import Author, Quote

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote

class AuthorSerializer(serializers.ModelSerializer):
    quotes = QuoteSerializer(read_only=True, many=True)

    class Meta:
        model = Author

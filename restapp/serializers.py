
from rest_framework import serializers
from .models import books

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = ['id', 'title', 'description']

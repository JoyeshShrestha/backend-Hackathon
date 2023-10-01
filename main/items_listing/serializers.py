# serializers.py

from rest_framework import serializers
from .models import ItemListing

class ItemListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemListing
        fields = '__all__'  # Include all fields from the model

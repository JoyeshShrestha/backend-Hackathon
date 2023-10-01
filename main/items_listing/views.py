# views.py

from rest_framework import viewsets
from .models import ItemListing
from .serializers import ItemListingSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response


from rest_framework.views import APIView


from django.http import JsonResponse
from django.views import View
from .models import ItemListing
from .serializers import ItemListingSerializer

import jwt

class ItemListingViewSet(viewsets.ModelViewSet):
    queryset = ItemListing.objects.all()
    serializer_class = ItemListingSerializer

class GetAllItemsView(View):
    def get(self, request, *args, **kwargs):
        # Retrieve all items from the database
        items = ItemListing.objects.all()

        # Serialize the items using the ItemListingSerializer
        serializer = ItemListingSerializer(items, many=True)

        # Return the serialized items as JSON response
        return JsonResponse(serializer.data, safe=False)




from rest_framework.response import Response
from rest_framework.views import APIView

from matchat.models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.

class pay_check(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
from rest_framework.response import Response
from rest_framework.views import APIView

from matchat.models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from django.shortcuts import render

# Create your views here.

class pay_check(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(key = 96144)
        serializer = ProductSerializer(products, many=True)
        if request.method == "POST":
            return Response("111", request.key, serializer.data)
        return Response("000", serializer.data)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api_finish.serializers import *
from matchat.models import *

class Result(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# Create your views here.

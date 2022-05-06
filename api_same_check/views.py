from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api_same_check.serializers import *
from matchat.models import *
from rest_framework import status


class PostList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

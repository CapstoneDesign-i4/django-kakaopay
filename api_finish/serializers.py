from rest_framework import serializers
from matchat.models import *

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('state', 'key')
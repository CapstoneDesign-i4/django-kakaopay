from rest_framework.views import APIView
from rest_framework.response import Response
from api_same_check.serializers import *
from matchat.models import *
from rest_framework import status

class ProductList(APIView):
    # 모든 데이터 가져오기 (API Test용)
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class Result(APIView):
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)

        # 유효성 검사
        if serializer.is_valid():
            key = serializer.validated_data['key']  # key에 값 저장
            try:
                product = Product.objects.get(key=key)  # 해당 key를 가진 상품 호출
            except Product.DoesNotExist:
                product = None

            if product == None:
                data = {'status': '2'}
                return Response(data)

            # 해당 key를 가진 상품에, 사진 url과 kiosk_result 저장
            product.kiosk_photo = serializer.validated_data['kiosk_photo']
            product.kiosk_result = serializer.validated_data['kiosk_result']
            product.save()

            # web_result == kiosk_result 이면 1 반환, 아니면 0 반환
            if product.web_result == product.kiosk_result:
                data = {'status': '1'}
                return Response(data)
            else:
                data = {'status': '0'}
                return Response(data)


from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'use_period', 'price', 'content', 'lock_num', 'place']
        labels = {
            'name': '상품명',
            'use_period': '사용기간',
            'price': '가격',
            'content': '설명',
            'lock_num': '사물함 비밀번호',
            'place': '지점',
        }

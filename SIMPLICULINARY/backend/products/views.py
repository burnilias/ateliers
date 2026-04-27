from django.shortcuts import render
from django.views import View
from .data import products

class ProductListView(View):
    def get(self, request):
        return render(request, 'products/product_list.html', {'produits': products})
from django.shortcuts import render
from django.views.generic import ListView

from app.products.models import Product


class ProductListView(ListView):
    """"
    View to display all products
    """
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

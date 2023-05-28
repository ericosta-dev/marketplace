from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Product, Category

from .forms import CategoryForm, ProductForm


class ProductListView(ListView):
    """"
    View to display all products
    """
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    """
    View to create a new product
    """
    model = Product
    template_name = 'product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('products-list')
    success_message = 'Produto adicionado com sucesso!'

class CategoryListView(ListView):
    """"
    View to display all categories
    """
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    """
    View to create a new category
    """
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('categories-list')
    success_message = 'Categoria adicionada com sucesso!'

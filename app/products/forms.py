from django import forms
from .models import Category, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image_url', 'stock_quantity', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter the product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Enter the product description',
                                            'rows': 3, 'cols': 40}),
            'price': forms.NumberInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter the product price'}),
            'image_url': forms.FileInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter the product image url'}),
            'stock_quantity': forms.NumberInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter the product stock quantity'}),
            'category': forms.Select(attrs={'class': 'form-control',
                                            'placeholder': 'Enter the product category'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter the category name'}),
        }

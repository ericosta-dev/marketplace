from django.urls import include, path

from .views import ProductListView,ProductCreateView, CategoryListView, CategoryCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='products-list'),
    path('add/', ProductCreateView.as_view(), name='product-add'),
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
]

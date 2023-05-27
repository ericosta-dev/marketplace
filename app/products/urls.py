from django.urls import include, path

from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
]

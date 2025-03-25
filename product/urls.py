from django.urls import path
from .views import ProductView

app_name = "products"

urlpatterns = [
    path('products/', ProductView.as_view(), name='product-list'),  # GET (all) и POST
    path('products/<int:pk>/', ProductView.as_view(), name='product-detail'),  # GET (one), PUT, DELETE
]
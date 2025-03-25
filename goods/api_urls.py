from rest_framework import routers
from django.urls import path, include
from goods import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)


urlpatterns = [
    #Метод ApiView
    # path('products/', views.ProductList.as_view(), name='product-list'),
    # path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    # path('categories/', views.CategoryList.as_view(), name='category-list'),
    # path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),

    #Метод GenericApiView
    # path('products/', views.ProductListCreate.as_view(), name='product-list-create'),
    # path('products/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    # path('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    # path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy'),

    #viewsets
    path('', include(router.urls)),
   

]
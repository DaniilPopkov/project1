from django.shortcuts import get_object_or_404,get_list_or_404,render
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,viewsets
from goods.models import Products,Categories
from goods.utils import q_search
from .serializers import ProductSerializer, CategorySerializer



def catalog(request,category_slug=None):

    page=request.GET.get('page',1)
    on_sale=request.GET.get('on_sale',None)
    order_by=request.GET.get('order_by',None)
    query=request.GET.get('q',None)

    if category_slug =='all':
        goods=Products.objects.all()
    elif query:
        goods=q_search(query)
    else:
        goods=get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods=goods.filter(discount__gt=0)
    if order_by and order_by !="default":
        goods=goods.order_by(order_by)

    paginator=Paginator(goods,2)
    current_page=paginator.page(int(page))

    context = {
        "title": "Sunrise - Меню",
        "goods":current_page,
        "slug_url":category_slug
    }
    return render(request, "goods/catalog.html",context)


def product(request,product_slug):

    product=Products.objects.get(slug=product_slug)

    context = {
        'product':product
    }

    return render(request, "goods/product.html",context=context)


#ApiView
# class ProductList(APIView):
#     """
#     Представление для получения списка всех продуктов и создания нового продукта.
#     """
#     def get(self, request):
#         products = Products.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except Exception as e:
#                  return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDetail(APIView):
#     """
#     Представление для получения, обновления и удаления информации об одном продукте.
#     """
#     def get(self, request, pk):
#         product = get_object_or_404(Products, pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         product = get_object_or_404(Products, pk=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data)
#             except Exception as e:
#                  return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         product = get_object_or_404(Products, pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CategoryList(APIView):
#     """
#     Представление для получения списка всех категорий и создания новой категории.
#     """
#     def get(self, request):
#         categories = Categories.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except Exception as e:
#                  return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CategoryDetail(APIView):
#     """
#     Представление для получения, обновления и удаления информации об одной категории.
#     """
#     def get(self, request, pk):
#         category = get_object_or_404(Categories, pk=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         category = get_object_or_404(Categories, pk=pk)
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data)
#             except Exception as e:
#                  return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         category = get_object_or_404(Categories, pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#GenericApiView
# class ProductListCreate(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

# class CategoryListCreate(generics.ListCreateAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategorySerializer

# class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
   

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
  


from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})

    def post(self, request):
        product = request.data.get('products')
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
            return Response({"success": "Product '{}' created successfully".format(product_saved.name)})
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, pk):
        saved_product = get_object_or_404(Product.objects.all(), pk=pk)
        
        serializer = ProductSerializer(instance=saved_product, data=request.data, partial=True) 
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
            return Response({
                "success": "Product '{}' updated successfully".format(product_saved.name)
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({"success": "Product with id '{}' deleted successfully".format(pk)}, status=status.HTTP_204_NO_CONTENT)

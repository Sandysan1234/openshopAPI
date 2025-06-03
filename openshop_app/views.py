from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from openshop_app.serializers import ProductSerializer
from .models import Product


# Create your views here.
class Product_list(APIView):
    def post(self, request):
        product = ProductSerializer(data=request.data, context={'request': request})
        if product.is_valid(raise_exception=True):
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        name = request.query_params.get('name', None)

        if name:
            products = Product.objects.filter(name__icontains=name, is_delete=False)
        else:
            products = Product.objects.filter(is_delete=False)

        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response({"products": serializer.data}, status=status.HTTP_200_OK)

class Product_detail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk, is_delete=False)

        except Product.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk, is_delete=False)
        except Product.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        product.is_delete = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

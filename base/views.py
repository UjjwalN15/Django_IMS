from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.

class DepartmentApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductCategoryApiView(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
class SupplierApiView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
class PurchaseApiView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    def get(self,request):
        queryset = self.get_queryset()
        serializer= self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Created!")
        else:
            return Response(serializers.errors)
        
class PurchaseDetailApiView(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, pk):
        try:
            queryset = Product.objects.get(id=pk)
        except:
            return Response("Product Not Found",status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            queryset = Product.objects.get(id=pk)
        except:
            return Response("Product Not Found",status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Updated!")
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            queryset = Product.objects.get(id=pk)
        except:
            return Response("Product Not Found",status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response("Data Deleted!")
    
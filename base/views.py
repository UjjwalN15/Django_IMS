from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
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
class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
    
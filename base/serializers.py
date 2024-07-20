from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password', 'groups']
        
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [ 'name']
        
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__' 

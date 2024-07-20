from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from .models import *
from .serializers import *
from .permissions import CustomPermissions
from django.contrib.auth.models import Group
# from django.db.models import Q  => Need for OR clause
# Create your views here.

class DepartmentApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    search_fields = ['name']
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #WE dont need to do anything in filtering in ModelViewSet
    filterset_fields = ['category','department']
    search_fields = ['name']
    #OR CLause
    #For OR clause you need to comment this code: filterset_fields = ['category','department']
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     category = self.request.query_params.get('category')
    #     department = self.request.query_params.get('department')
    
    #     if category and department:
    #         queryset = queryset.filter(Q(category=category) | Q(department=department))
    #     elif category:
    #         queryset = queryset.filter(category=category)
    #     elif department:
    #         queryset = queryset.filter(department=department)
    #     return queryset

class ProductCategoryApiView(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    # def get(self, request):
    #     queryset = self.get_queryset()
    #     filter_queryset = self.filter_queryset(queryset)
    #     serializer= self.serializer_class(filter_queryset,many=True)
    #     return Response(serializer.data)
    #OR For Filtering you just can do: filterset_fields = ['category','department'] <= The filtering is done with category an department
    #In ModelViewSet
    search_fields = ['name']
class SupplierApiView(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    search_fields = ['name']
class PurchaseApiView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filterset_fields = ['product','supplier']
    search_fields = ['name']
    def get(self,request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer= self.serializer_class(filter_queryset,many=True)
        return Response(serializer.data)
    #In GenericAPIView, we need to define a get method function because filtering is all about getting values
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class PurchaseDetailApiView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    search_fields = ['name']
    def get(self, request, pk):
        try:
            queryset = Purchase.objects.get(id=pk)
        except:
            return Response("Product Not Found",status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            queryset = Purchase.objects.get(id=pk)
        except:
            return Response("Product Not Found",status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            queryset = Purchase.objects.get(id=pk)
        except:
            return Response("Product Not Found",status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response("Data Deleted!")
    
    def patch(self, request,pk=None):
        queryset = self.get_object()
        serializer = PurchaseSerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny,]) #This permission class should always below the api view
def Login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=email, password=password)
    if user == None:
        return Response("Invalid Credentials",status=status.HTTP_404_NOT_FOUND)
    else:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    
@api_view(['POST'])
@permission_classes([AllowAny,]) #This permission class should always below the api view
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hash_password = make_password(password)
        a = serializer.save()
        a.password = hash_password
        a.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([AllowAny,]) #This permission class should always below the api view
def groups(request):
    groups_obj = Group.objects.all()
    serializer = GroupSerializer(groups_obj, many = True)
    return Response(serializer.data)

class ReportViewSet(ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer
    search_fields = ['title']

    def list(self, request):
        users_count = User.objects.count()
        products_count = Product.objects.count()
        report = {
            'users_count':users_count,
            'total_products':products_count
        }
        return Response(report)


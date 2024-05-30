from django.urls import path
from .views import *

urlpatterns = [
    path('department/', DepartmentApiView.as_view({'get': 'list','post':'create'}),name='department'),
    path('department/<int:pk>/', DepartmentApiView.as_view({'get': 'retrieve', 'put':'update', 'delete':'destroy'}),name='department'),
    path('product/', ProductApiView.as_view({'get': 'list','post':'create'}),name='product'),
    path('product/<int:pk>/', ProductApiView.as_view({'get': 'retrieve', 'put':'update', 'delete':'destroy'}),name='product'),
    path('product_category/', ProductCategoryApiView.as_view({'get': 'list','post':'create'}),name='product_category'),
    path('product_category/<int:pk>/', ProductCategoryApiView.as_view({'get': 'retrieve', 'put':'update', 'delete':'destroy'}),name='product_category'),
    path('supplier/', SupplierApiView.as_view({'get': 'list','post':'create'}),name='supplier'),
    path('supplier/<int:pk>/', SupplierApiView.as_view({'get': 'retrieve', 'put':'update', 'delete':'destroy'}),name='supplier'),
    path('purchase/', PurchaseApiView.as_view({'get': 'list','post':'create'}),name='purchase'),
    path('purchase/<int:pk>/', PurchaseApiView.as_view({'get': 'retrieve', 'put':'update', 'delete':'destroy'}),name='purchase'),
]
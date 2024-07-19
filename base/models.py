from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=200, default = 'username')
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
class ProductCategory(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name #returns the name in admin panel
    
    
class Department(models.Model):
    name = models.CharField(max_length = 200)
    floor = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    stock = models.IntegerField()
    category = models.ForeignKey(ProductCategory,on_delete = models.SET_NULL, null = True)
    department = models.ManyToManyField(Department)
    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    
class Purchase(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    # product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)  CASCADE removes all the data when the Department is deleted
    product = models.ForeignKey(Product,on_delete = models.CASCADE) #models.SET_NULL replaces the NUll value if Product is deleted
    supplier = models.ForeignKey(Supplier,on_delete = models.SET_NULL, null = True) 
    


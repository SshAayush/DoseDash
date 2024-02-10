from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    Product_Name = models.CharField(max_length = 200)
    Product_Price = models.PositiveIntegerField(null = False)
    Product_Description = models.TextField()
    Product_Tag = models.CharField(max_length = 100)
    Product_Image = models.ImageField(upload_to = 'static/image/products/')
    
    def __str__(self):
        return self.Product_Name
    
class Cart(models.Model):
    Cart_Details = models.ForeignKey(Product, on_delete=models.CASCADE, blank= True, null= True)
    Cart_Quantity = models.PositiveIntegerField(null = False)
    User_Details = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    
    def __str__(self):
        return self.Cart_Details.Product_Name
    
class Transaction(models.Model):
    Transaction_ID = models.CharField(max_length = 200)
    Transaction_Amount = models.PositiveIntegerField(null = False)
    Transaction_Date = models.DateTimeField(auto_now_add=True)
    User_Details = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    Transaction_Status = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.Transaction_ID
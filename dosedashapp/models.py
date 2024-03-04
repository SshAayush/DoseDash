from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductTag(models.Model):
    tag = models.CharField(max_length = 100)
    def __str__(self):
        return self.tag
    
class Product(models.Model):
    Product_Name = models.CharField(max_length = 200)
    Product_Price = models.PositiveIntegerField(null = False)
    Product_Description = models.TextField()
    Product_Tag = models.ManyToManyField(ProductTag, blank = True)
    Product_Image = models.ImageField(upload_to = 'static/image/products/')
    Product_Quantity = models.PositiveBigIntegerField(null = True)
    
    def __str__(self):
        return self.Product_Name
    
class Cart(models.Model):
    Cart_Details = models.ForeignKey(Product, on_delete=models.CASCADE, blank= True, null= True)
    Cart_Quantity = models.PositiveIntegerField(null = False)
    User_Details = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    
    def __str__(self):
        return self.User_Details.username + " - " +self.Cart_Details.Product_Name
    
class Transaction(models.Model):
    Transaction_ID = models.CharField(max_length = 200)
    Transaction_Amount = models.PositiveIntegerField(null = False)
    Transaction_Date = models.DateTimeField()
    User_Details = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    Transaction_Status = models.CharField(max_length = 300)
    Item_Pruchased = models.ManyToManyField(Product, blank = True)
    Payment_Method = models.CharField(max_length = 300, blank=True)
    
    def __str__(self):
        return self.User_Details.username + " - " + self.Transaction_ID
    
class Reminder(models.Model):
    Reminder_UserName = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    Reminder_ProductId = models.ForeignKey(Product, on_delete=models.CASCADE, null= True, blank= True)
    Reminder_Date = models.DateTimeField()
    
    def __str__(self):
        return self.Reminder_UserName.username + " - " + self.Reminder_ProductId.Product_Name
    
class ContactUs(models.Model):
    Customer_Name = models.CharField(max_length = 200)
    Customer_Email = models.EmailField(max_length = 200)
    Customer_Message = models.TextField()
    
    def __str__(self):
        return self.Customer_Name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone_Number = models.CharField(max_length=15, blank=True, null=True)
    Country = models.CharField(max_length=200, blank=True, null=True)
    Province = models.CharField(max_length=200, blank=True, null=True)
    City = models.CharField(max_length=200, blank=True, null=True)
    Area = models.CharField(max_length=200, blank=True, null=True)
    Landmark = models.CharField(max_length=200, blank=True, null=True)
    Image = models.ImageField(upload_to = 'static/image/user/')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_name = models.DateTimeField()

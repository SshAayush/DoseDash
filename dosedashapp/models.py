from django.db import models

# Create your models here.
class Product(models.Model):
    Product_Name = models.CharField(max_length = 200)
    Product_Price = models.PositiveIntegerField(null = False)
    Product_Description = models.TextField()
    Product_Tag = models.CharField(max_length = 100)
    Product_Image = models.ImageField(upload_to = 'static/image/products/')
    
    def __str__(self):
        return self.Product_Name
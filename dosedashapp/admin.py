from django.contrib import admin
from .models import Product,Cart,Transaction

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Transaction)

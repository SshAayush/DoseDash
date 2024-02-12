from django.contrib import admin
from .models import Product,Cart,Transaction,Reminder,ProductTag

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Transaction)
admin.site.register(Reminder)
admin.site.register(ProductTag)

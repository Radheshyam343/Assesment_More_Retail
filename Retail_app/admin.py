from django.contrib import admin
from .models import Product_record,Transaction_record

# Register your models here.
admin.site.register(Product_record)

admin.site.register(Transaction_record)
from django.contrib import admin
from .models import Product, Order

# 1. Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock') 
    list_filter = ('category',)
    search_fields = ('name', 'description')

# 2. Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'customer_name', 'phone', 'email', 'product', 'quantity', 'status', 'created_at')
    
    list_filter = ('status', 'created_at')
    
   
    search_fields = ('customer_name', 'phone', 'email', 'product')
    
    
    list_editable = ('status',)
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, MenuItem, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity', 'order_date')
    list_filter = ('order_date',)
    search_fields = ('menu_item__name',)


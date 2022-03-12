from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Class for the product model
    """
    list_display = ('name', 'category', 'description',
                    'price', 'rating', 'image', 'image_url')
    list_filter = ('name', 'category', 'price')
    search_fields = ('name', 'category', 'price')





admin.site.register(Product, ProductAdmin)

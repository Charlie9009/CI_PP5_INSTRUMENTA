from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """
    Class for the product model
    """
    list_display = ('name', 'category', 'description',
                    'price', 'rating', 'image', 'image_url',)
    list_filter = ('name', 'category', 'price',)
    search_fields = ('name', 'category', 'price',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Class for the category model
    """
    list_display = ('friendly_name', 'name',)


class ReviewAdmin(admin.ModelAdmin):
    """
    Class for the product model
    """
    list_display = ('user', 'product', 'comment',
                    'rating', 'created_on',)
    list_filter = ('user', 'product', 'comment', 'rating',)
    search_fields = ('user', 'product', 'comment', 'rating',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)

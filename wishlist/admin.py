from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    """
    Admin class for the Favourites model.
    """
    list_display = ('user',)
    search_fields = ('user', 'products',)
    list_filter = ('user', 'products',)


admin.site.register(Wishlist, WishlistAdmin)

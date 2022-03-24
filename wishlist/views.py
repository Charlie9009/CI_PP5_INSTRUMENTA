from django.shortcuts import render
from .models import Wishlist


def wishlist(request):
    """
    View to render all wishlist items
    """
    try:
        wishlist_objects = Wishlist.objects.filter(user=request.user.id)[0]
        wishlist_items = wishlist_objects.products.all()
    except IndexError:
        wishlist_items = None
    template = 'wishlists/wishlist.html'
    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, template, context)

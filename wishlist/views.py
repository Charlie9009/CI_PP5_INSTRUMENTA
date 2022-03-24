from django.shortcuts import render


def wishlist(request):
    """
    View to render all wishlist items
    """
    template = 'wishlists/wishlist.html'

    return render(request, template)
    
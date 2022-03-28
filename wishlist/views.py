from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Wishlist, Product


@login_required
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


@login_required
def add_to_wishlist(request, item_id):
    """
    Add a product item to wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        wishlists = get_object_or_404(Wishlist, user=request.user.id)
    except Http404:
        wishlists = Wishlist.objects.create(user=request.user)
    if product in wishlists.products.all():
        messages.error(
                       request,
                       'You already have this product in your wishlist')
    else:
        wishlists.products.add(product)
        messages.info(request, 'You added this product to your wishlist')
    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def remove_from_wishlist(request, item_id):
    """
    View to remove a product from wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    wishlists = get_object_or_404(Wishlist, user=request.user.id)
    if product in wishlists.products.all():
        wishlists.products.remove(product)
        messages.info(
                      request,
                      'Removed the product from your wishlist')
    else:
        messages.error(request, 'Ops, something went wrong')
    return redirect(reverse('wishlist'))

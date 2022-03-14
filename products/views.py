from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ A view to show products and search the page """

    products = Product.objects.all()
    query = None
    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, 'You did not enter any search criteria!')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return the product_detail page, a single product. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


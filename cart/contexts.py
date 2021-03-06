from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Product


def cart_contents(request):
    """
    Esures cart contents are available
    to view on any page within our collection of apps.
    """
    cart = request.session.get('cart', {})

    cart_items = []
    sub_total = 0
    total = 0
    product_count = 0

    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        sub_total = quantity * product.price
        total += quantity * product.price
        product_count += quantity

        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count
        }

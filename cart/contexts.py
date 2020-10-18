from django.shortcuts import get_object_or_404
from products.models import Product


def cart_items(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for key, value in cart.items():
        product = get_object_or_404(Product, pk=key)
        cart_items.append(
            {
                'product': product,
            }
        )
    return {
        'cart_items': cart_items,
    }


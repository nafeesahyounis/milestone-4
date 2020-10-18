from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.


def cart(request):
    """A view to return the checkouttest page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        print(f"cart {cart}")
        product = get_object_or_404(Product, pk=product_id)
        print(product)
        cart[product.id] = 1
        request.session['cart'] = cart

        print(cart)
        context = {'item': product}
        print(context)
        return render(request, 'cart/cart.html', cart)
    else:
        return render(request, 'cart/cart.html', context)









from django.shortcuts import render, get_object_or_404
from .models import Cart
from products.models import Product

# Create your views here.


def checkouttest(request):
    """A view to return the checkouttest page"""
    return render(request, 'checkout/checkouttest.html')


def update_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        print(cart)
        product = get_object_or_404(Product, pk=product_id)
        print(product)
        cart[product_id] = 1
        request.session['cart'] = cart

        print(cart)
        context = {'item': product}
        print(context)
        return render(request, 'checkout/checkouttest.html', context)
    else:
        return render(request, 'checkout/checkouttest.html', context)









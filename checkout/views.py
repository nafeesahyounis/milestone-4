from django.shortcuts import render, get_object_or_404
from .models import Cart
from products.models import Product

# Create your views here.


def checkouttest(request):
    """A view to return the checkouttest page"""
    return render(request, 'checkout/checkouttest.html')


def update_cart(request, product_id):
    if request.method == 'POST':

        cart = Cart.objects.all()[0]
        product = get_object_or_404(Product, pk=product_id)
        cart.products.add(product)
        context = {'cart': cart}
        print(context)
        return render(request, 'checkout/checkouttest.html', context)
    else:
        return render(request, 'checkout/checkouttest.html', context)









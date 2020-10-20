from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm

# Create your views here.


def checkouttest(request):
    """A view to return the checkouttest page"""
    return render(request, 'checkout/checkouttest.html')


def create_order(request):

    cart = request.session.get('cart', {})

    print(cart)
    return render(request, 'checkout/checkouttest.html')















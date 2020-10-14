from django.shortcuts import render
from .models import Cart

# Create your views here.

def checkouttest(request):
    """A view to return the checkouttest page"""
    cart = Cart.objects.all()[0]
    context = {'cart': cart}
    return render(request, 'checkout/checkouttest.html', context)
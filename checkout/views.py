from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.


def checkouttest(request):
    """A view to return the checkouttest page"""
    return render(request, 'checkout/checkouttest.html')










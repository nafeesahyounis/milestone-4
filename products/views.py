from django.shortcuts import render
from .models import Product

# Create your views here.

def test(request):
    """A view to return the test page"""
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/test.html', context)
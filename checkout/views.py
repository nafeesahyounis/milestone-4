from django.shortcuts import render

# Create your views here.

def test(request):
    """A view to return the checkouttest page"""
    return render(request, 'checkout/checkouttest.html')
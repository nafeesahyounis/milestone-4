from django.shortcuts import render

# Create your views here.

def checkouttest(request):
    """A view to return the checkouttest page"""
    return render(request, 'checkout/checkouttest.html')
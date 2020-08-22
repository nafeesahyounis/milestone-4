from django.shortcuts import render

# Create your views here.

def test(request):
    """A view to return the index page"""
    return render(request, 'products/test.html')
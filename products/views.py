from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def test(request):

    if request.method == "POST":
        filter = (request.POST)
        products = Category.objects.filter(name__exact=filter)

        context= {
            'products': products,
        }

    else:
        """A view to return the test page"""
        products = Product.objects.all()
        context = {
        'products': products,
        }
    return render(request, 'products/test.html', context)

#post name of category
#
from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def test(request):

    if request.method == "POST":

        # filter = (request.POST)
        query = request.POST
        print(query)
        products = Product.objects.filter(category='1')

        context = {
            'products': products,
        }
        return render(request, 'products/test.html', context)

    else:
        """A view to return the test page"""
        products = Product.objects.all()
        context = {
        'products': products,
        }
    return render(request, 'products/test.html', context)


#post name of category
#
from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def test(request):

    categories = Category.objects.all()
    print(categories)

    if request.method == "POST":

        # filter = (request.POST)
        query = request.POST
        print('this is being printed', query)
        products = Product.objects.filter(category=query)
        print(products)

        context = {
            'products': products,
        }
        return render(request, 'products/test.html', context)

    else:
        """A view to return the test page"""
        products = Product.objects.all()
        context = {
        'products': products,
        'categories': categories
        }
    return render(request, 'products/test.html', context)


#post name of category
#
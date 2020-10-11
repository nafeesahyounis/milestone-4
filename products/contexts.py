from django.shortcuts import render
from .models import Product


def sort(request, id, currentCategory):
    
    query = request.POST['sort']
    currentCategory = currentCategory
    products = Product.objects.filter(category=id)
    context = {
            'products': products,
        }
    if query == '1':
        products = products.order_by('price')
        context = {
            'products': products,
            'currentCategory': currentCategory,
        }
        return render(request, 'products/test.html', context)
    if query == '2':
        products = products.order_by('price').reverse()
        print('result descending', products)
        context = {
            'products': products,
            'currentCategory': currentCategory,

            }
        return render(request, 'products/test.html', context)
    if query == '3':
        products = products.order_by('rating').reverse()
        print('rating', products)
        context = {
            'products': products,
            'currentCategory': currentCategory,

        }
        return render(request, 'products/test.html', context)

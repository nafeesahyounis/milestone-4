from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def test(request):

    categories = Category.objects.all()
    print(categories)

    if request.method == "POST":

        # filter = (request.POST)
        #if request.POST['sort']
        #query = request.POST['category']
        #print('this is being printed', query)
        #products = Product.objects.filter(category=query)
        #print(products)
        query = request.POST['sort']
        print('this is being printed', query)
        products = Product.objects.all()
        context = {
                'products':products,
            }
        if query == 1:
            products = products.order_by('price')
            print('result ascending',products)
            context = {
                'products':products,
            }
            return render(request,'products/test.html', context)
        else:
            products = products.order_by('price').reverse()
            print('result descending',products)
            context = {
                'products': products,
            }
            return render(request,'products/test.html', context)
        


    else:
        """A view to return the test page"""
        products = Product.objects.all()
        context = {
        'products': products,
        'categories': categories
        }
    return render(request, 'products/test.html', context)

def stylists(request):
    
    products = Product.objects.filter(category='1')
    context = {
            'products': products,
        }
    return render(request, 'products/test.html', context)

def interiordesigners(request):
    
    products = Product.objects.filter(category='2')
    context = {
            'products': products,
        }
    return render(request, 'products/test.html', context)

def personaltrainers(request):
    
    products = Product.objects.filter(category='5')
    category = personaltrainers
    context = {
            'products': products,
        }
    return render(request, 'products/test.html', context, category)

def professionalphotos(request):
    
    products = Product.objects.filter(category='4')
    context = {
            'products': products,
        }
    return render(request, 'products/test.html', context)

def lifecoaches(request):
    
    products = Product.objects.filter(category='3')
    context = {
            'products': products,
        }
    return render(request, 'products/test.html', context)

def other(request):
    
    products = Product.objects.filter(category='6')
    context = {
            'products': products,
        }
    return render(request, 'products/test.html', context)



#post name of category
#
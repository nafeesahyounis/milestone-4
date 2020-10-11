from django.shortcuts import render
from .models import Product, Category
from products.contexts import sort

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
        currentCategory = 'test'
        products = Product.objects.all()
        context = {
                'products':products,
            }
        if query == '1':
            products = products.order_by('price')
            print('result ascending',products)
            context = {
                'products':products,
                'currentCategory':currentCategory,
            }
            print("1")
            return render(request,'products/test.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            print('result descending',products)
            context = {
                'products': products,
            }
            print("2")
        if query == '3':
            products = products.order_by('rating').reverse()
            print('rating',products)
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            print("3")
            return render(request, 'products/test.html', context)
        


    else:
        """A view to return the test page"""
        products = Product.objects.all()
        currentCategory ='test'

        context = {
         'products': products,
         'currentCategory': currentCategory,
        }
        
        return render(request, 'products/test.html', context)

        

def stylists(request):

    products = Product.objects.filter(category='1')

    if request.method == "POST":

        query = request.POST['sort']
        print('this is being printed', query)
        currentCategory = 'stylists'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            print('result ascending',products)
            context = {
                'products':products,
                'currentCategory':currentCategory,
            }
            print("1")
            return render(request,'products/test.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            print('result descending',products)
            context = {
                'products': products,
                'currentCategory':currentCategory,

            }
            return render(request, 'products/test.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
            print('rating',products)
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            return render(request, 'products/test.html', context)
        


    else:
        """A view to return the test page"""
        products = Product.objects.filter(category='1')
        currentCategory ='stylists'

        context = {
         'products': products,
         'currentCategory': currentCategory,
        }
        
        return render(request, 'products/test.html', context)

def interiordesigners(request):

    products = Product.objects.filter(category='2')
    if request.method =="POST":

        sort(request,2, interiordesigners)
    else:
        """A view to return the test page"""
        products = Product.objects.filter(category='2')
        currentCategory ='interiordesigners'

        context = {
         'products': products,
         'currentCategory': currentCategory,
        }
        
        return render(request, 'products/test.html', context)


    
def personaltrainers(request):
    
    products = Product.objects.filter(category='5')
    currentCategory ='personaltrainers'

    context = {
            'products': products,
            'currentCategory': currentCategory
        }
    return render(request, 'products/test.html', context)

def professionalphotos(request):
    
    products = Product.objects.filter(category='4')
    context = {
            'products': products,
        }
    return render(request, 'products/test.html', context)

def lifecoaches(request):
    
    products = Product.objects.filter(category='3'),
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


def listing(request):
    
    
    return render(request, 'products/listing.html')


#post name of category
#
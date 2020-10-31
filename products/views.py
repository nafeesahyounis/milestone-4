from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from products.contexts import sort

# Create your views here.

def products(request):
    categories = Category.objects.all()
    print(categories)

    if request.method == "POST":
        
        query = request.POST['sort']
        currentCategory = 'products'
        products = Product.objects.all()
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            print('result ascending', products)
            context = {
                'products': products,
                'currentCategory': currentCategory,
            }
            print("1")
            return render(request, 'products/test.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            print('result descending', products)
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            print("2")
            return render(request, 'products/products.html', context)

        if query == '3':
            products = products.order_by('rating').reverse()
            print('rating',products)
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            print("3")
            return render(request, 'products/products.html', context)
    else:
        """A view to return the test page"""
        products = Product.objects.all()
        currentCategory = 'products'

        context = {
            'products': products,
            'currentCategory': currentCategory,
        }
        
        return render(request, 'products/products.html', context)   

def stylists(request):
    products = Product.objects.filter(category='2')
    print(products)
    if request.method == "POST":
        query = request.POST['sort']
        print('this is being printed', query)
        currentCategory = 'stylists'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            print('result ascending', products)
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            print("1")
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            print('result descending', products)
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
            print('rating', products)
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            return render(request, 'products/products.html', context)
        


    else:
        """A view to return the test page"""
        products = Product.objects.filter(category='2')
        currentCategory ='stylists'

        context = {
         'products': products,
         'currentCategory': currentCategory,
        }
        
        return render(request, 'products/products.html', context)


def interiordesigners(request):

    products = Product.objects.filter(category='1')

    if request.method == "POST":
        query = request.POST['sort']
        print('this is being printed', query)
        currentCategory = 'interiordesigners'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            print('result ascending', products)
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            print("1")
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            print('result descending', products)
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
            print('rating', products)
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            return render(request, 'products/products.html', context)
    
    else:
        currentCategory = 'interiordesigners'

        context = {
            'products': products,
            'currentCategory': currentCategory,
            }
        
        return render(request, 'products/products.html', context)
 
    
def personaltrainers(request):
    
    products = Product.objects.filter(category='3')
    if request.method == "POST":
        query = request.POST['sort']
        print('this is being printed', query)
        currentCategory = 'personaltrainers'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            print('result ascending', products)
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            print("1")
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            print('result descending', products)
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
            print('rating', products)
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            return render(request, 'products/products.html', context)
    
    else:
        currentCategory = 'personaltrainers'

        context = {
            'products': products,
            'currentCategory': currentCategory,
            }
        
        return render(request, 'products/products.html', context)
 
   

def professionalphotos(request):
    
    products = Product.objects.filter(category='5')
    if request.method == "POST":
        query = request.POST['sort']
        print('this is being printed', query)
        currentCategory = 'professionalphotos'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            print('result ascending', products)
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            print("1")
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            print('result descending', products)
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
            print('rating', products)
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            return render(request, 'products/products.html', context)
    
    else:
        currentCategory = 'professionalphotos'

        context = {
            'products': products,
            'currentCategory': currentCategory,
            }
        
        return render(request, 'products/products.html', context)
 
    
def lifecoaches(request):
    
    products = Product.objects.filter(category='4'),
    context = {
            'products': products,
        }
    return render(request, 'products/products.html', context)




def listing(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    currentCategory = product.category
    print('category', type(currentCategory))
    result = str(currentCategory)
    print('result', result)
    context = {
            'product': product,
            'currentCategory': currentCategory,
            'result': result
                }
    return render(request, 'products/listing.html', context)


def categories(request):
    return render(request, 'products/categories.html')


#post name of category
#
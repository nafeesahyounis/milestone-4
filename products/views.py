from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.


def products(request):

    if request.method == "POST":

        query = request.POST['sort']
        currentCategory = 'products'
        products = Product.objects.all()
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
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            return render(request, 'products/products.html', context)

        if query == '3':
            products = products.order_by('rating').reverse()
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
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
    if request.method == "POST":
        query = request.POST['sort']
        currentCategory = 'stylists'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            return render(request, 'products/products.html', context)
    else:
        """A view to return the test page"""
        products = Product.objects.filter(category='2')
        currentCategory = 'stylists'

        context = {
         'products': products,
         'currentCategory': currentCategory,
        }

        return render(request, 'products/products.html', context)


def interiordesigners(request):

    products = Product.objects.filter(category='1')

    if request.method == "POST":
        query = request.POST['sort']
        currentCategory = 'interiordesigners'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
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
        currentCategory = 'personaltrainers'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
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
        currentCategory = 'professionalphotos'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
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
    if request.method == "POST":
        query = request.POST['sort']
        currentCategory = 'lifecoaches'
        context = {
                'products': products,
            }
        if query == '1':
            products = products.order_by('price')
            lowToHigh = "Products are now listed from highest to lowest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': lowToHigh
            }
            return render(request, 'products/products.html', context)
        if query == '2':
            products = products.order_by('price').reverse()
            highToLow = "Products are now listed from lowest to highest price"
            context = {
                'products': products,
                'currentCategory': currentCategory,
                'filter': highToLow

            }
            return render(request, 'products/products.html', context)
        if query == '3':
            products = products.order_by('rating').reverse()
            context = {
                'products': products,
                'currentCategory': currentCategory,

            }
            return render(request, 'products/products.html', context)

    else:
        """A view to return the test page"""
        products = Product.objects.filter(category='4')
        currentCategory = 'lifecoaches'

        context = {
         'products': products,
         'currentCategory': currentCategory,
        }

        return render(request, 'products/products.html', context)


def listing(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    currentCategory = product.category
    result = str(currentCategory)
    context = {
            'product': product,
            'currentCategory': currentCategory,
            'result': result
                }
    return render(request, 'products/listing.html', context)


def categories(request):
    return render(request, 'products/categories.html')


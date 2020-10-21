from django.shortcuts import render,redirect,reverse, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from products.models import Product

# Create your views here.


def checkouttest(request):
    """A view to return the checkouttest page"""
    return render(request, 'checkout/checkouttest.html')


def create_order(request):

    cart = request.session.get('cart', {})

    print('cart printed', cart)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for key, value in cart.items():
                try:
                    product = Product.objects.get(id=key)
                    print('product:', product)
                    if isinstance(value, int):
                        order_line_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=value,
                        )
                        order_line_item.save()
                        print('saved', order_line_item)
                    else:
                        print('we are jumping')

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('checkout/order_created.html'))
    else:
        form = OrderCreateForm()
        (print, 'else clause')
        return render(request, 'checkout/order_created.html', {'cart': cart, 'form': form})
                    
            # clear the cart
            #cart.clear()
            #return render(request,
            #              'checkout/order_created.html',
            #              {'order': order})
   # else:
   #     form = OrderCreateForm()
   # return render(request,
   #               'checkout/order_created.html',
   #               {'cart': cart, 'form': form})















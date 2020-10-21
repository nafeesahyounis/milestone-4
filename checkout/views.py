from django.shortcuts import render, redirect,reverse
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
            order.save()

            for key, value in cart.items():
                try:
                    product = Product.objects.get(id=key)
                    print('product:', product)
                    if isinstance(value, int):
                        print('am being executed')
                        print(product)
                        print(order)
                        print(value)
                        print('order item', OrderItem)
                        order_line_item = OrderItem(order=order,
                                                    product=product,
                                                    quantity=value,)
                        print('beginning', order_line_item)
                        #order_line_item.order = order
                        # order_line_item.save()
                        #print('next line', order_line_item)
                        #order_line_item.product = product
                        #order_line_item.quantity = value
                        order_line_item.save()
                        print('save')
                        print('test', order_line_item)
                        #order_line_item = OrderItem(
                        #    order=order,
                        #    product=product,
                        #    quantity=value,
                        #)
                        #print('before', order_line_item)
                        #order_line_item.save()
                        print('saved', order_line_item)
                    else:
                        print('we are jumping')

                except Product.DoesNotExist:
                    print('does not exist')
                    
                    order.delete()
                    return render(request, 'checkout/order_created.html')
            return render(request, 'checkout/order_created.html')
        return render(request, 'checkout/order_created.html')


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















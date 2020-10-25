from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.conf import settings
from .models import OrderItem, Order
from .forms import OrderCreateForm
from products.models import Product
from django.contrib import messages
from cart.contexts import cart_items
import stripe 
# Create your views here.


def checkouttest(request):
    """A view to return the checkouttest page"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse('test'))
    
    for key, value in cart.items():
        product = Product.objects.get(id=key)
        print('price', product.price)
        # TO SELF: ADD FUNCTIONALITY THAT ADDS BOTH VALUES TOGETHER. CURRENTLY ONLY TAKES ONE. FIX THISSSSS
        total_cost = product.price
    print(total_cost)
    stripe_total = round(total_cost*100)
    stripe.api_key = stripe_secret_key
    print(stripe_secret_key)
    print('public key', stripe_public_key)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    client_secret = intent.client_secret
    print('client secret print', client_secret)

    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing \
        Did you forget to set it in your environment?")

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    } 
    return render(request, 'checkout/checkouttest.html', context)


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
                        print('price', product.price)
                        total_cost = product.price
                        print('order item', OrderItem)
                        order_line_item = OrderItem(order=order,
                                                    product=product,
                                                    quantity=value,
                                                    total_cost=total_cost)
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
                    return render(request, 'checkout/order_created.html', order_line_item)
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




def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)
    print('order number', order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)











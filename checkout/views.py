from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm

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
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            return render(request,
                          'checkout/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'checkout/order_created.html',
                  {'cart': cart, 'form': form})















from django.shortcuts import render, redirect,reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import OrderItem
from .forms import OrderCreateForm
from products.models import Product
from django.contrib import messages
from cart.contexts import cart_items
import stripe
# Create your views here.
#create a form with the order for users who are not logged in (add login functionality later)


@ login_required
def checkouttest(request):
    """A view to return the checkouttest page"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    #create order form
    form = OrderCreateForm()
    #create session cart
    cart = request.session.get('cart', {})
    #if the cart is empty, redirect to products
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse('products'))
    #if the user submits the form, an order is created in the database

    if request.method == 'POST':
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                order.save()

                for key, value in cart.items():
                    try:
                        product = Product.objects.get(id=key)
                        if isinstance(value, int):
                            total_cost = product.price
                            order_line_item = OrderItem(order=order,
                                                        product=product,
                                                        quantity=value,
                                                        total_cost=total_cost)
                            order_line_item.save()
                        else:
                            print('we are jumping')

                    except Product.DoesNotExist:
                        order.delete()
                        return redirect(reverse('cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        # save session info to be used in checkout_success
        for key, value in cart.items():
            product = Product.objects.get(id=key)
        # TO SELF: ADD FUNCTIONALITY THAT ADDS BOTH VALUES TOGETHER. CURRENTLY ONLY TAKES ONE. FIX THISSSSS
            total_cost = product.price
        stripe_total = round(total_cost*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,)
        form = OrderCreateForm()
        client_secret = intent.client_secret

        if not stripe_public_key:
            messages.warning(request, "Stripe public key is missing \
            Did you forget to set it in your environment?")

        context = {
            'stripe_public_key': stripe_public_key,
            'client_secret': client_secret,
            'form': form,

        } 
        return render(request, 'checkout/checkouttest.html', context)


def checkout_success(request):
    """
    Handle successful checkouts
    """
    messages.success(request, f'Order successfully processed! \
        Your order number is ____. A confirmation \
        email will be sent to.')
    if 'cart' in request.session:
        del request.session['cart']
    template = 'checkout/checkout_success.html'
    return render(request, template)











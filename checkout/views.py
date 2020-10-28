from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Bag is empty")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HhNceJAHu7MS8QLq8c3Ry6GeFk06zWLYZYCiqyMnWIGIgxciWa3TKsl4KUawfpnOi2XfzsvgjLzuLWLUbhj7v6k00eQmEDBUe',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

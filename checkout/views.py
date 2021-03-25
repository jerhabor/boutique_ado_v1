from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IYr5HFpDro4uo9WuTFZvYanp1iizOj85ANzqh3iQidCHSdFeRFe6iYv1S20A3ycjM4nwCA9Bpy8IE48M8eVBa4g00yjzzxNVz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

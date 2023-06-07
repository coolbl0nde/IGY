from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from pharmacy_app.models import Medicines
from .cart import Cart
from .forms import CartAddCarForm
from django.core.exceptions import PermissionDenied


@require_POST
def cart_add(request, medicines_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("No acsess")

    cart = Cart(request)
    medicines = get_object_or_404(Medicines, id=medicines_id)
    form = CartAddCarForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(medicines=medicines,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, medicines_id):
    if not request.user.is_authenticated:
        raise PermissionDenied("No acsess")

    cart = Cart(request)
    medicines = get_object_or_404(Medicines, id=medicines_id)
    cart.remove(medicines)
    return redirect('cart:cart_detail')


def cart_detail(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("No acsess")
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
from django.shortcuts import render
from .models import OrderItem
#from .forms import OrderCreateForm
from cart.cart import Cart
from pharmacy_app.models import Client
from .models import Order
from django.core.exceptions import PermissionDenied


def order_create(request):

    if not request.user.is_authenticated:
        raise PermissionDenied("No access")

    cart = Cart(request)
    if request.method == 'POST':        
        order = Order.objects.create(client = Client.objects.filter(email=request.user.email).first())

        for item in cart:
            OrderItem.objects.create(order=order,
                                        medicines=item['medicines'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            item['medicines'].purchase_count += item['quantity']
            item['medicines'].save()
        # очистка корзины
        cart.clear()
        return render(request, 'order/created.html',
                        {'order': order})
    
    return render(request, 'order/create.html',
                  {'cart': cart})
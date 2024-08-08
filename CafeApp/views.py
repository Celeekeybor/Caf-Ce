from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render, get_object_or_404
from .models import MenuItem, Order

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})

def place_order(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')
        menu_item = get_object_or_404(MenuItem, id=item_id)
        order = Order(menu_item=menu_item, quantity=quantity)
        order.save()
        return render(request, 'order_success.html', {'order': order})
    return render(request, 'place_order.html')

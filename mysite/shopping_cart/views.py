from django.shortcuts import render


from products.models import Product_model
from . import models
# Create your views here.
def cart_detail(request, total=0, counter=0, cart_items = None):
    one_order = get_object_or_404(Product_model,pk=id)
    # all_products = models.Product_model.objects.all()
    cart_items = models.Product_model.objects.get()
    for cart_item in cart_items:
        total += (cart_item.price * cart_item.quantity)
        counter += cart_item.quantity
        context = {
        "one_order": one_order,
        "total": total,
        "counter": counter,
        "cart_items": cart_items,
        }
    return render(request, 'cart.html', context=context)


        # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

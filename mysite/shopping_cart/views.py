from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from accounts.forms import Registration_form
from products.models import Product_model
from . import models
# Create your views here.


def pending_order(request):
    order = models.Shopping_cart_model.objects.filter(username=request.user,is_ordered=False)
    # user_name = get_object_or_404(Shopping_cart_model, username=request.user)
    if order.exists():
        return order[0]
    return 0

def cart_detail(request, total=0, counter=0, cart_items = None):
    one_order = models.Shopping_cart_model.objects.all()

    # user_name = get_object_or_404(Shopping_cart_model, username=request.user)
    # order = Order_model.objects.filter(is_ordered=False)
    existing_order = pending_order(request)
    # order = models.Shopping_cart_model.objects.filter(username=request.user,is_ordered=False)
    # all_products = models.Product_model.objects.all()
    # one_order = models.Shopping_cart_model.objects.all()

    # cart_items = models.Product_model.objects.all()
    #
    # for cart_item in cart_items:
    #     total += cart_item.price #* cart_item.quantity)
    #     counter += cart_item.stock

    context = {
    "existing_order": existing_order,
    "one_order": one_order,
    # "total": total,
    # "counter": counter,
    # "cart_items": cart_items,
    # "user_name": user_name,
    }
    return render(request, 'shopping_cart/shopping_cart.html', context=context)
    #     # get order for the correct user
    # user_profile = get_object_or_404(Profile, user=request.user)
    # order = Order_model.objects.filter(is_ordered=False)
    # if order.exists():
    #     # get the only order in the list of filtered orders
    #     return order[0]
    # return 0



@login_required()
def cart_add(request, product_id):
    # get the user profile
    # user_profile = get_object_or_404(User, user=request.user)
    # filter products by id
    add_product = Product_model.objects.filter(id=product_id).first()
    # check if the user already owns this product
    # if product in request.user.profile.ebooks.all():
    #     messages.info(request, 'You already own this ebook')
    #     return redirect(reverse('products:product-list'))
    # create orderItem of the selected product
    order_item, status = models.Shopping_cart_item_model.objects.get_or_create(product=add_product)
    # create order associated with the user
    user_order, status = models.Shopping_cart_model.objects.get_or_create(username=user_profile, is_ordered=False)
    # user_order.items.add(order_item)
    # if status:
    #     # generate a reference code
    #     user_order.ref_code = generate_order_id()
    #     user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect('/shopping_cart/')

# def cart_add(request, product_id):
    # order_item, status = Shopping_cart_item_model.objects.get_or_create(product=product)
    # id = get_object_or_404(Product_model,pk=product_id)
    # # order_item, created = Product_model.objects.get_or_create(product=product)
    # create_order, created = Order_model.objects.get_or_create(is_ordered=True)
    # # OrderItem_model.product.items.add(order_item)
    # add_item = models.Shopping_cart_item_model.objects.all()
    # for x in add_item:
    #     price += x.product.price
    #     x.quantity += 1
    #     Shopping_cart_item_model.save()
    # messages.info(request, "Item added to cart")
    # return redirect('/shopping_cart/')
    # return HttpResponse("Item added to cart")
    #
    #
    # # get the user profile
    # user_profile = get_object_or_404(Profile, user=request.user)
    # # filter products by id
    # product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    # # check if the user already owns this product
    # if product in request.user.profile.ebooks.all():
    #     messages.info(request, 'You already own this ebook')
    #     return redirect(reverse('products:product-list'))
    # # create orderItem of the selected product
    # order_item, status = OrderItem.objects.get_or_create(product=product)
    # # create order associated with the user
    # user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    # user_order.items.add(order_item)
    # if status:
    #     # generate a reference code
    #     user_order.ref_code = generate_order_id()
    #     user_order.save()
    #
    # # show confirmation message and redirect back to the same page
    # messages.info(request, "item added to cart")
    # return redirect(reverse('products:product-list'))



# def cart_remove(request, product_id):
#     item_to_delete = Shopping_cart_item_model.product.id.objects.filter(pk=product_id)
#     try:
#         book = Book.objects.get(pk=)
#     execpt ObjectDoesNotExist:
#         pass
#     else:
#         cart = Shopping_cart_model.objects.get()
#         cart.remove_from_cart(product_id)
#     return redirect('cart')

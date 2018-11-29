from django.shortcuts import render, get_object_or_404


from products.models import Product_model
from . import models
# Create your views here.
def products_detail(request,product_id):
    all_products = models.Product_model.objects.all()
    single_item = get_object_or_404(Product_model,pk=product_id,available=True)
    context = {
    "all_products":all_products,
    "single_item":single_item,
    }
    return render(request, 'descriptions.html', context=context)

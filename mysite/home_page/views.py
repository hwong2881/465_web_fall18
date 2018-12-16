from django.shortcuts import render

from products.models import Product_model
from products.models import Category_model


from . import models
# Create your views here.
def home(request):
    all_products = models.Product_model.objects.all()
    all_catrgories = models.Category_model.objects.all()
    #
    # msg = ""
    # all_products = models.Product_Model.objects.all()
    # query = request.GET.get("q")
    # if request.method == 'GET':
    #     form_instance = forms.SearchForm(request.GET)
    #     if query:
    #         results = models.Product_Model.objects.filter(name__icontains=query)
    #         msg = "was found"
    #     else:
    #         form_instance = forms.SearchForm()
    #         results = models.Product_Model.objects.all()
    #         msg = "was not found"
    context = {
    "all_products":all_products,
    # "form_instance":form_instance,
    # "results":results,
    # "msg":msg,
    "all_catrgories":all_catrgories,
    }
    return render(request, 'home_page/home_page.html', context=context)

def category(request, category):
    if request.method == 'GET':
        find_catrgory = models.Product_model.objects.get(category=category)
        context = {
        "find_catrgory":find_catrgory,
        }
    return redirect('/')

from django.db import models

from django.contrib.auth.models import User
from products.models import Product_model


# Create your models here.
class Shopping_cart_item_model(models.Model):
    product = models.ForeignKey(Product_model, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Shopping_cart_model(models.Model):
    ref_code = models.CharField(max_length=15)
    username = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(Shopping_cart_item_model)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.username, self.ref_code)

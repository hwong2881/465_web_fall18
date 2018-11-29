from django.db import models
from products.models import Product_model
from products.models import Category_model

# Create your models here.
class SearchModel(models.Model):
    search = models.CharField(max_length=100)

    def __str__(self):
        return self.search

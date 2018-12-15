from django.db import models

# Create your models here.


class Checkout_model(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    # gender =
    # street = models.TextField()
    zipcode = models.IntegerField(default=True)
    shipping_method = models.BooleanField(default=True)

    def get_absolute_url(self):
        return "/products/%i/" % self.id

    def __str__(self):
        return self.first_name

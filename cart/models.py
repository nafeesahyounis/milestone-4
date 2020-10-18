from django.db import models
from products.models import Product

# Create your models here.


class Cart(models.Model):
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


    def __unicode__(self):
        return "Cart if %s" % (self.id)
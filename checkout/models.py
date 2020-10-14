from django.db import models
from products.models import Product

# Create your models here.

class Cart(models.Model):

    product = models.ManyToManyField(Product, null=True, blank=True),
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return "Cart if %s" % (self.id)
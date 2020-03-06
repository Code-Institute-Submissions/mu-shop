from django.db import models
from products.models import Product
from decimal import Decimal
from django.db.models import Sum

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    sub_total = models.FloatField(blank=False)

    def total(self):
        x = str(self.product.price)
        y = x.translate({ord(i): None for i in '€'})
        z = y.translate({ord(i): None for i in ','})
        new_total = float(z)
        sub_total = new_total * self.quantity
        return sub_total

    def __str__(self):
        return "{0} {1} @ {2} - {3}".format(self.order.id, self.quantity, self.product.name, self.product.price)


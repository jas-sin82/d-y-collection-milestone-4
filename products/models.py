from django.db import models
from django.utils import timezone
from django.db.models import Avg, Count, Sum
from decimal import Decimal

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    
    GENDER = [
        ('f', 'f'), 
        ('m', 'm'),
    ]

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    size = models.BooleanField(default=False, null=True, blank=True)
    discount_percent = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    average_rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    image_a = models.ImageField(null=True, blank=True)
    image_b = models.ImageField(null=True, blank=True)
    image_c = models.ImageField(null=True, blank=True)
    image_d = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
from django.db import models
from django.utils import timezone
from django.db.models import Avg, Count, Sum
from django.contrib.auth.models import User
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


class Brand(models.Model):

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
    brand = models.ForeignKey('Brand', null=True, blank=True,
                              on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    on_sale = models.BooleanField(default=False)
    size = models.BooleanField(default=False, null=True, blank=True)
    discount_percent = models.DecimalField(
        max_digits=2, decimal_places=0, null=True, blank=True)
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

    # credit to : https://helperbyte.com/questions/77886/django
    # how-to-make-a-discount-for-the-item
    # Calculate price with discount percentage
    def sale_price(self):

        sale = Decimal(self.price * (
            100 - self.discount_percent) / 100).quantize(Decimal('0.00'))

        return sale


class ProductReview(models.Model):
    """
    Product Review Model
    """

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Product Reviews'

    RATING = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    product = models.ForeignKey(Product, related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    review_text = models.TextField()
    review_rating = models.IntegerField(choices=RATING, default=5)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
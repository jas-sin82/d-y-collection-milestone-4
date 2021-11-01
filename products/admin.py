from django.contrib import admin
from .models import Product, Category, ProductReview, Brand

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'gender',
        'image_a',


    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'product', 'review_text', 'review_rating', 'date_added')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)

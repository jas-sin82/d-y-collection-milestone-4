from django import template
from decimal import Decimal


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


# Sub total calculation for sale price
@register.filter(name='calc_subtotal_offer')
def calc_subtotal_offer(sale_price, quantity):
    return sale_price * quantity
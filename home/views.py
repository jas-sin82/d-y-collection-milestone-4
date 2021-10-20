from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
    """ A view to return the index page """
    
    products = Product.objects.order_by('-date_added').all()[:8]
   
    template = 'home/index.html'
    context = {
        'products': products,
        
    }
    return render(request, template, context)
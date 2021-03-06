from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Brand, ProductReview
from .forms import ProductForm, ReviewForm


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    gender = None
    brands = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(gender__in=gender)
            gender = Product.objects.filter(gender__in=gender)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter \
                    any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brands': brands,
        'current_gender': gender,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()

    # to get related products of men's
    related_products_men = Product.objects.filter(
        category=product.category).exclude(
        sku=product.sku).order_by('-gender')[:4]

    # to get related products of women's
    related_products_women = Product.objects.filter(
        category=product.category).exclude(
        sku=product.sku).order_by('gender')[:4]

    context = {
        'product': product,
        'related_products_men': related_products_men,
        'related_products_women': related_products_women,
        'form': form,
    }

    return render(request, 'products/product_detail.html', context)


# A view to display all products on sale include sorting.
def sale_products(request):

    sort = None
    direction = None
    products = Product.objects.filter(on_sale=True)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}+{direction}'

    context = {
        'products': products,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/sale_products.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
            Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
            Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Allow users to add  a product review """

    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, 'Thank You! Your review \
                    has been successfully added!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'something went wrong! \
                    Please try to add your review again.')
    context = {
        'form': form
    }
    return render(request, context)


@login_required
def delete_review(request, review_id):
    """ Delete review """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry,just store owner can do that.')
        return redirect(reverse('home'))
    elif request.user.is_superuser:
        review = ProductReview.objects.filter(pk=review_id).last()
        product_id = review.product_id
        review.delete()
        messages.success(request, f"{ review.user }'s review has been \
        removed!", extra_tags=' ')
        return redirect(reverse('product_detail', args=[product_id]))

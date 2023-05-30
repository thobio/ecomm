from django.shortcuts import render
from products.models import Product

# Create your views here.


def get_products(request, slug):
    try:
        products = Product.objects.get(slug=slug)
        return render(request, 'product/product.html', {'product': products})
    except Exception as e:
        print(e)

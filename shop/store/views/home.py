from django.shortcuts import render
from django.views import View

from shop.store.models import Product, ReviewRating


class HomeView(View):
    def get(self, request):
        products = Product.objects.all().filter(is_available=True).order_by('created_date')

        # Get the reviews
        reviews = None
        for product in products:
            reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

        context = {
            'products': products,
            'reviews': reviews,
        }
        return render(request, 'home.html', context)
from django.shortcuts import render
from products.models import Product
from django.contrib import messages
from django.db.models import Q


def do_search(request):
    q = request.GET['results']
    products = Product.objects.filter(
        Q(name__icontains=q) |
        Q(description_line_one__icontains=q) |
        Q(description_line_two__icontains=q) |
        Q(description_line_three__icontains=q) |
        Q(description_line_four__icontains=q) |
        Q(short_description__icontains=q)
        )

    search = len(products)

    if search == 0:
        messages.success(request, "{} Search results found".format(search))
    else:
        messages.success(request, "{} Search results found".format(search))

    return render(
        request, "products.html", {
            'products': products, 'search': search
            }
            )

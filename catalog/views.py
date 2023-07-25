from django.shortcuts import render

from catalog.models import Product, Contact


def index(request):
    # Convert QuerySet to List
    list_products = list(Product.objects.all())
    # Print last five records
    if len(list_products) >= 5:
        for product in list_products[-5:]:
            print(product)
    else:
        for product in list_products:
            print(product)
    return render(request, 'index.html')

    # Get all products from catalog
def category_list(request):
    products = list(Product.objects.all())

    context = {
        'list_products': products,
    }

    return render(request, 'category_list.html', context)


def contacts(request):
    data = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'contacts.html',{"contacts": data})

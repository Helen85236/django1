from django.shortcuts import render

from catalog.models import Product, Contact, Category


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
    context = {
        'object_list': list_products,
    }
    return render(request, 'index.html', context)

    # Get all products from catalog
def category_list(request):
    category = list(Category.objects.all())

    context = {
        'list_products': category,
    }

    return render(request, 'category_list.html', context)

def product(request,id_product):
    product = Product.objects.get(id=id_product)

    context = {
        'object': product,
    }

    return render(request, 'product_detail.html', context)



def contacts(request):
    data = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'contacts.html',{"contacts": data})

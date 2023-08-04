from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from catalog.models import Product, Contact, Category


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


# def index(request):
#     # Convert QuerySet to List
#     list_products = list(Product.objects.all())
#     # Print last five records
#     # if len(list_products) >= 5:
#     #     for product in list_products[-5:]:
#     #         print(product)
#     # else:
#     #     for product in list_products:
#     #         print(product)
#     # context = {
#     #     'object_list': list_products,
#     # }
#     return render(request, 'index.html', context)
#
#     # Get all products from catalog

def category_list(request):
    category = list(Category.objects.all())

    context = {
        'list_products': category,
    }

    return render(request, 'category_list.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

# def product(request,id_product):
#     product = Product.objects.get(id=id_product)
#
#     context = {
#         'object': product,
#     }
#
#     return render(request, 'product_detail.html', context)



def contacts(request):
    data = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'contacts.html',{"contacts": data})

from django.urls import path

from catalog.views import index, contacts, category_list, product

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('category/', category_list),
    path('product/<int:id_product>', product),
]
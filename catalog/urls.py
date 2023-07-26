from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, category_list, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category_list),
    path('product/<int:id_product>', product),
]
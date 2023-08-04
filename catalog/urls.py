from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ProductDetailView, contacts, category_list # product

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category_list),
    path('product/<int:id_product>', ProductDetailView.as_view(), name='product'),
]
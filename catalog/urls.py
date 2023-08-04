from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, ProductDetailView, contacts, CategotyListView, BlogListView, BlogCreateView # product

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('category/', CategotyListView.as_view(), name='category_list'),
    path('product/<int:id_product>', ProductDetailView.as_view(), name='product'),
]
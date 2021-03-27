from django.urls import path

from .views import index
from .views import ItemListView
from .views import ItemDetailView


urlpatterns = [
    path('', index, name='index'),
    path('items/', ItemListView.as_view(), name='item_list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]

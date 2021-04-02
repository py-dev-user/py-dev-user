from django.urls import path

from .views import index
from .views import ItemListView
from .views import ItemDetailView
from .views import UserProfileView, update_profile


urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    path('accounts/profile/update/', update_profile, name='profile-update'),
    path('items/<str:tag_name>/', ItemListView.as_view(), name='items_by_tag'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/', ItemListView.as_view(), name='item_list'),

]

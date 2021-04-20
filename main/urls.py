from django.urls import path

from .views import index
from .views import ItemListView
from .views import ItemDetailView
# from .views import UserProfileView, update_profile
from .views import ItemCreateView, ItemUpdateView, ItemDeleteView
from .views import send_message_to_email


urlpatterns = [
    path('', index, name='index'),
    path('send_message/', send_message_to_email, name='send_msg'),
    # path('accounts/profile/<int:pk>', UserProfileView.as_view(), name='profile'),
    # path('accounts/profile/update/', update_profile, name='profile-update'),
    path('item/create/', ItemCreateView.as_view(), name='create-item'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='update-item'),
    # path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='delete-item'),
    path('items/<str:tag_name>/', ItemListView.as_view(), name='items_by_tag'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('items/', ItemListView.as_view(), name='item_list'),
]

from django.urls import path

from .views import profile_view
from .views import profile_update


urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
]

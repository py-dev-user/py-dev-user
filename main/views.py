from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from .models import ItemModel, TagModel, Profile
from .forms import UserForm, ProfileForm


def index(request):
    turn_on_block = True
    return render(request, 'main/index.html', {'turn_on_block': turn_on_block})


class ItemListView(ListView):
    model = ItemModel
    paginate_by = 5

    def get_queryset(self):
        try:
            tag = get_object_or_404(TagModel, tag=self.kwargs['tag_name'])
            return ItemModel.objects.filter(tag=tag.id, published=1)
        except KeyError as ex:
            return ItemModel.objects.filter(published=1)


class ItemDetailView(DetailView):
    model = ItemModel


class UserProfileView(DetailView):
    model = Profile


# позже заменю на класс
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('profile', args=[user_form.instance.id]))
        else:
            messages.error(request, _('Please fix issues: '))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/profile_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

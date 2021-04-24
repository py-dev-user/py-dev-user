from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import ItemModel, TagModel # , Profile
from .models import SellerModel
# from .forms import UserForm, ProfileForm
from .forms import SendMessage

from py_dev_user.utilities import send


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


# class UserProfileView(DetailView):
#     model = Profile
#
#
# # позже заменю на класс
# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return HttpResponseRedirect(reverse('profile', args=[user_form.instance.id]))
#         else:
#             messages.error(request, _('Please fix issues: '))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'main/profile_form.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })


class ItemCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'main.add_item'
    model = ItemModel
    fields = '__all__'


class ItemUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'main.change_item'
    model = ItemModel
    fields = '__all__'


class ItemDeleteView(PermissionRequiredMixin, DeleteView):
    pass


@login_required
def send_message_to_email(request):
    if request.method == 'POST':
        form = SendMessage(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            is_seller = bool(form.cleaned_data['is_seller'])

            if is_seller:
                recipients = SellerModel.objects.filter(is_active=True).exclude(email='').values('email')
            else:
                recipients = (User.objects.filter(is_active=True).
                              exclude(email='').exclude(is_staff=True).values('email'))

            if len(recipients) > 0:
                recipients = [element['email'] for element in recipients]

            send(subject, body, recipients)

            return HttpResponseRedirect(reverse('index'))
    else:
        form = SendMessage()

    return render(request, 'main/send_message.html', {'form': form})

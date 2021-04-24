from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ProfileForm
from .models import Profile


def index(request):
    return render(request, 'account/index.html')


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'account/profile.html', {'user': user})


@login_required
def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(Profile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.birthdate = form.cleaned_data['birthdate']
            user_profile.location = form.cleaned_data['location']
            user_profile.phone_number = form.cleaned_data['phone_number']
            user_profile.avatar = request.FILES.get('avatar')   # form.cleaned_data['avatar']
            user_profile.save()

            return HttpResponseRedirect(reverse('profile'))
    else:
        data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'birthdate': user_profile.birthdate,
            'location': user_profile.location,
            'phone_number': user_profile.phone_number,
            'avatar': user_profile.avatar
        }

        form = ProfileForm(data)

    return render(request, 'account/profile_update.html', {'form': form, 'user': user})

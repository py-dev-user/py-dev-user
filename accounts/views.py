from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.urls import reverse

import main.views


def sign_up(request):
    context = {}

    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='common users')
            group.user_set.add(user)

            return HttpResponseRedirect(reverse('login'))

    context['form'] = form

    return render(request, 'registration/sign_up.html', context)

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.urls import reverse

import main.views


def sign_up(request):
    context = {}
    group_name = 'common users'

    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            groups = Group.objects.filter(name=group_name)
            if len(groups) > 0:
                group = groups[0]
            else:
                group = Group(name=group_name)
                group.save()
            group.user_set.add(user)

            return HttpResponseRedirect(reverse('login'))

    context['form'] = form

    return render(request, 'registration/sign_up.html', context)

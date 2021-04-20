from django import forms
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['avatar'] = forms.ImageField()

    def clean(self):
        return self.cleaned_data

    # def save(self, request):
    #     email = self.cleaned_data['email']
    #     users = User.objects.filter(email=email)
    #     if users:
    #         return users[0]
    #
    #     user = super(MyForm, self).save(request)
    #     return user

    def custom_signup(self, request, user):
        group_name = 'common users'

        user.email = self.cleaned_data['email']
        # user.is_active = False
        user.save()

        groups = Group.objects.filter(name=group_name)
        if len(groups) > 0:
            group = groups[0]
        else:
            group = Group(name=group_name)
            group.save()
        group.user_set.add(user)

        user.profile.avatar = self.cleaned_data['avatar']
        user.profile.save()
        return user


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50, required=False)
    last_name = forms.CharField(label='Last name', max_length=50, required=False)
    birthdate = forms.DateField(label='Birthdate', required=False)
    location = forms.CharField(label='Location', max_length=50, required=False)
    avatar = forms.ImageField(label='Avatar', required=False)

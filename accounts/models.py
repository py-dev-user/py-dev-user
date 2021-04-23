from allauth.account.utils import perform_login
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.signals import pre_social_login
from allauth.account.signals import user_signed_up
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile/', null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    last_updated_time = models.DateTimeField('Last modified', auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class Sender(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    is_active = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    email_address = sociallogin.account.extra_data['email']
    users = User.objects.filter(email=email_address)
    if users:
        perform_login(request, users[0], email_verification='optional')
        raise ImmediateHttpResponse(redirect(settings.LOGIN_REDIRECT_URL.format(id=request.user.id)))


@receiver(user_signed_up)
def send_activation_email(request, user, **kwargs):
    print('User registered')

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import Profile
from .models import Sender


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

    def avatar_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}"  />'.format(
            url=obj.avatar.url,
            width=300,
            # height=obj.avatar.height,
        )
    )

    readonly_fields = ["avatar_image"]


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
    list_select_related = ('profile', )

    def get_location(self, instance):
        return instance.profile.location
    get_location.short_description = 'Location'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class SenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Sender, SenderAdmin)

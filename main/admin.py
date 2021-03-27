from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from .models import ItemModel
from .models import AdditionalImage
from .models import CategoryModel
from .models import TagModel
from .models import SellerModel
from .models import CurrencyModel

from ckeditor.widgets import CKEditorWidget


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    list_display = ('url', 'title', 'template_name')


class SellerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'date_joined')
    fields = (
        ('username', 'password',),
        ('first_name', 'last_name'),
        ('email', 'phone'),
        ('is_active'),
        ('last_login', 'date_joined'),
    )

    readonly_fields = ('last_login', 'date_joined')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name')


class ExtraImagesAdmin(admin.ModelAdmin):
    list_display = ('image', 'item')


class ExtraImagesInline(admin.TabularInline):
    model = AdditionalImage
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'category', 'price', 'currency', 'seller', 'published', 'item_create', 'item_update')
    fields = (
        ('short_name', 'seller'),
        'description',
        ('category', 'published', 'in_stock'),
        ('price', 'currency'),
        'tag',
        'image'
    )

    inlines = (ExtraImagesInline,)
    actions = ['activate_item', 'deactivate_item']

    def activate_item(self, request, queryset):
        row_update = queryset.update(published=True)
        if row_update == 1:
            message_bit = 'One item was updated'
        else:
            message_bit = f'{row_update} items were updated'

        self.message_user(request, f'{message_bit}')

    def deactivate_item(self, request, queryset):
        row_update = queryset.update(published=False)
        if row_update == 1:
            message_bit = 'One item was updated'
        else:
            message_bit = f'{row_update} items were updated'

        self.message_user(request, f'{message_bit}')

    activate_item.short_description = 'Activate'
    activate_item.allowed_permission = ('change',)

    deactivate_item.short_description = 'Deactivate'
    deactivate_item.allowed_permission = ('change',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)

admin.site.register(ItemModel, ItemAdmin)
admin.site.register(AdditionalImage, ExtraImagesAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(TagModel)
admin.site.register(SellerModel, SellerAdmin)
admin.site.register(CurrencyModel, CurrencyAdmin)

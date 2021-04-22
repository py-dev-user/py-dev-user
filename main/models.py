from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

from py_dev_user.utilities import get_timestamp_path


class CategoryModel(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='Name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Parent category')
    published = models.BooleanField(verbose_name='Published', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'


class TagModel(models.Model):
    tag = models.CharField(max_length=50, verbose_name='Tag')
    published = models.BooleanField(verbose_name='Published', default=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Tag'


class CurrencyModel(models.Model):
    full_name = models.CharField(max_length=25, verbose_name='Полное имя')
    short_name = models.CharField(max_length=5, verbose_name='Короткое имя')

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = 'Currency'


class SellerModel(User):
    phone = models.CharField(max_length=25, verbose_name='Phone', null=True, blank=True)

    class Meta:
        verbose_name = 'Seller'


class ItemModel(models.Model):
    short_name = models.CharField(max_length=100, verbose_name='Object name', db_index=True)
    description = RichTextField()
    image = models.ImageField(verbose_name='Image', blank=True, null=True, upload_to=get_timestamp_path)
    tag = models.ManyToManyField(TagModel, blank=True)
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField(verbose_name='Price', default=0.0)
    currency = models.ForeignKey(CurrencyModel, on_delete=models.SET_NULL, blank=True, null=True)
    published = models.BooleanField(verbose_name='Published', default=True)
    in_stock = models.BooleanField(verbose_name='In stock', default=True)
    item_create = models.DateTimeField(auto_now_add=True, verbose_name='created')
    item_update = models.DateTimeField(auto_now=True, verbose_name='updated')

    def __str__(self):
        return self.short_name

    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()

        super().delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Item'
        ordering = ['-item_create']


class AdditionalImage(models.Model):
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE, verbose_name='Item')
    image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Image')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Additional imge'
        verbose_name_plural = 'Additional images'


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ItemReports(models.Model):
    item = models.OneToOneField(ItemModel, on_delete=models.CASCADE)
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return self.item.short_name

    class Meta:
        verbose_name = 'Item report'
        ordering = ['-is_send']

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(verbose_name='Avatar', blank=True, null=True, upload_to=get_timestamp_path)
#     date_of_birth = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return ''   # self.user.username
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


@receiver(post_save, sender=ItemModel)
def create_item_dispatcher(sender, **kwargs):
    item = kwargs['instance']
    item_reports = ItemReports()
    item_reports.item = item
    item_reports.save()

# Generated by Django 3.1.7 on 2021-04-04 21:50

from django.db import migrations, models
import main.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210402_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=main.utilities.get_timestamp_path, verbose_name='Avatar'),
        ),
    ]

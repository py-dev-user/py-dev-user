# Generated by Django 3.1.7 on 2021-03-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210326_2112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Currency',
            new_name='CurrencyModel',
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='price',
            field=models.FloatField(default=0.0, verbose_name='Price'),
        ),
    ]

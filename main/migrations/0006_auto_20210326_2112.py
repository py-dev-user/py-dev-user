# Generated by Django 3.1.7 on 2021-03-26 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmodel',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.currency'),
        ),
        migrations.AlterField(
            model_name='itemmodel',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
    ]

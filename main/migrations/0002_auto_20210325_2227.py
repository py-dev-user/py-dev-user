# Generated by Django 3.1.7 on 2021-03-25 22:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

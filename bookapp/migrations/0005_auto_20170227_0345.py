# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_auto_20170227_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(db_table='category_book', to='bookapp.Category'),
        ),
    ]

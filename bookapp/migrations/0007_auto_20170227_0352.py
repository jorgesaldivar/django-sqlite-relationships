# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0006_auto_20170227_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(db_table='%(app_label)s_%(class)s_related', to='bookapp.Category'),
        ),
    ]

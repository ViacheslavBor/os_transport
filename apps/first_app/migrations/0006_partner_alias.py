# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-01-09 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_remove_partner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='alias',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]

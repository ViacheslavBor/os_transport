# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-01-15 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_partner_alias'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='link1',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='order',
            name='link2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='link3',
        ),
    ]

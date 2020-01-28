# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-01-09 03:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0003_auto_20200108_1515'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='password',
        ),
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='partner',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-08 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_accountlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles', verbose_name='Profile picture'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 07:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0116_make_group_membership_unique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='project',
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]

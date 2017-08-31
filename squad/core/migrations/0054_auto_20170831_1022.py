# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-31 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_remove_projectstatus_previous'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuiteVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(blank=True, max_length=256, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('revision', models.CharField(blank=True, max_length=128, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suiteversions', to='core.Project')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='suiteversion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SuiteVersion'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-29 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('phno', models.IntegerField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=10000)),
            ],
        ),
    ]

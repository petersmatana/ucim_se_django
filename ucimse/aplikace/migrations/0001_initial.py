# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NejakaTabulka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('cislo', models.IntegerField()),
            ],
        ),
    ]

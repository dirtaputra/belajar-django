# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 00:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0002_coba'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Penerbit',
        ),
    ]

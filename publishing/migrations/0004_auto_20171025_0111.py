# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 01:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishing', '0003_auto_20171025_0057'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Penerbit',
            new_name='Author',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0015_auto_20180102_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='triplist',
            old_name='trip_number',
            new_name='trip_no',
        ),
    ]

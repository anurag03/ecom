# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-02 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20161102_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iteminfo',
            name='item_image1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
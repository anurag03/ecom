# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-02 09:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminfo',
            name='item_image1',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='item_image2',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='item_image3',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='item_image4',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='item_image5',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='item_image6',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='iteminfo',
            name='item_url',
            field=models.CharField(default=datetime.datetime(2016, 11, 2, 9, 54, 11, 949568, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
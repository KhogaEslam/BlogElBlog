# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_post_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, upload_to='./static/media/'),
        ),
    ]
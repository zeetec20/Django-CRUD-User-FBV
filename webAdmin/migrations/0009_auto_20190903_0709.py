# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-03 07:09
from __future__ import unicode_literals

from django.db import migrations, models
import webAdmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('webAdmin', '0008_auto_20190902_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='imagesGoods',
            field=models.ImageField(upload_to=webAdmin.models.Goods.upload_path_handler),
        ),
    ]

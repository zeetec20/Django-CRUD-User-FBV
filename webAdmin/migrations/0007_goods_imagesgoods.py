# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-02 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import webAdmin.models


class Migration(migrations.Migration):

    dependencies = [
        ('webAdmin', '0006_auto_20190902_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='imagesGoods',
            field=models.ImageField(default=0, upload_to=webAdmin.models.Goods.upload_path_handler),
            preserve_default=False,
        ),
    ]

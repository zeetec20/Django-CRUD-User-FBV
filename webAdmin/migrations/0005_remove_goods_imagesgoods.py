# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-02 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webAdmin', '0004_goods_rategoods'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='imagesGoods',
        ),
    ]
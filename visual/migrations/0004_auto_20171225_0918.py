# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0003_auto_20171222_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='name',
            field=models.CharField(default=b'', max_length=100, verbose_name='\u5bb9\u5668\u540d'),
        ),
    ]

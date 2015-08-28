# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_auto_20150820_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='first_name',
            field=models.CharField(max_length=40, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='record',
            name='last_name',
            field=models.CharField(max_length=40, verbose_name='Last Name'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_auto_20150827_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name_plural': 'records'},
        ),
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='record',
            name='first_name',
            field=models.CharField(verbose_name='First Name', max_length=40),
        ),
        migrations.AlterField(
            model_name='record',
            name='last_name',
            field=models.CharField(verbose_name='Last Name', max_length=40),
        ),
    ]

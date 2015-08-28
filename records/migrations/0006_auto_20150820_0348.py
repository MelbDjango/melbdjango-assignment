# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20150818_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='name',
        ),
        migrations.AddField(
            model_name='record',
            name='display',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='record',
            name='first_name',
            field=models.CharField(verbose_name='First Name', blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='record',
            name='last_name',
            field=models.CharField(verbose_name='Last Name', blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='record',
            name='email_address',
            field=models.EmailField(blank=True, max_length=40, help_text='*optional'),
        ),
    ]

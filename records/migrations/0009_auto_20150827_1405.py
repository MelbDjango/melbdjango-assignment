# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20150821_0030'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AlterModelOptions(
            name='record',
            options={},
        ),
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='record',
            name='display',
            field=models.BooleanField(choices=[(True, 'Show'), (False, 'Hide')], default=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='email_address',
            field=models.EmailField(help_text='*optional', max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='first_name',
            field=models.TextField(max_length=40, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='record',
            name='last_name',
            field=models.TextField(max_length=40, verbose_name='Last Name'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20150817_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='guest',
        ),
        migrations.AddField(
            model_name='record',
            name='name',
            field=models.CharField(max_length=200, default='Your awesome name'),
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]

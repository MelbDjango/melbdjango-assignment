# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_auto_20150827_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.TextField(max_length=400),
        ),
    ]

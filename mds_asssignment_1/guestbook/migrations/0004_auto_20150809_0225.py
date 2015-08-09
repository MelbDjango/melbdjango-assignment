# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0003_auto_20150808_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='comment',
            field=models.TextField(max_length=500),
        ),
    ]

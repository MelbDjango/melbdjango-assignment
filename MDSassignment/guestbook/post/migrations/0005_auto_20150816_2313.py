# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20150816_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=254, blank=True, null=True),
        ),
    ]

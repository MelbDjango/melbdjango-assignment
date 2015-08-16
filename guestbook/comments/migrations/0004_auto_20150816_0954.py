# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20150816_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.ForeignKey(to='comments.Comment'),
        ),
    ]

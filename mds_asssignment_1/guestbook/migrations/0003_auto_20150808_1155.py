# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_auto_20150808_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entry',
            name='email',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='lname',
            field=models.CharField(max_length=50, blank=True, verbose_name='Last Name'),
        ),
    ]

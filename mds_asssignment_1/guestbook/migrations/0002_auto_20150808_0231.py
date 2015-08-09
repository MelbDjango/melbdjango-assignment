# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='fname',
            field=models.CharField(verbose_name='First Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='entry',
            name='lname',
            field=models.CharField(verbose_name='Last Name', max_length=50),
        ),
    ]

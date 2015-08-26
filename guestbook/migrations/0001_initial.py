# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('name', models.CharField(max_length=60)),
                ('date', models.DateTimeField(db_index=True, auto_now=True)),
                ('hidden', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
    ]

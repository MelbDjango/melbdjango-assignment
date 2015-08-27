# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20150817_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=2000)),
                ('email_address', models.EmailField(max_length=254)),
                ('entry_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Your awesome name', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'records',
            },
        ),
        migrations.DeleteModel(
            name='Record',
        ),
    ]

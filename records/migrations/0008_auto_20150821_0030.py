# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_auto_20150820_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status', models.CharField(max_length=1, choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')])),
            ],
        ),
        migrations.AlterField(
            model_name='record',
            name='display',
            field=models.BooleanField(default=True, choices=[('t', True), ('f', False)]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('text', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('hidden_at', models.DateTimeField(null=True, blank=True)),
                ('is_spam', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]

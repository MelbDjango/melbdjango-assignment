# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.ForeignKey(to='post.Post')),
            ],
        ),
    ]

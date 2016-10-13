# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.CharField(max_length=6, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=4)),
            ],
        ),
    ]

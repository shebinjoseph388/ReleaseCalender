# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_auto_20190924_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseTypes',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('release_name', models.CharField(max_length=50)),
            ],
        ),
    ]

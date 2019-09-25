# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_releasetypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Releases',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.CharField(max_length=50)),
                ('end_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='releasetypes',
            name='id',
            field=models.AutoField(primary_key=True, max_length=10, serialize=False),
        ),
        migrations.AddField(
            model_name='releases',
            name='release_type',
            field=models.ForeignKey(to='Admin.ReleaseTypes'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def insertData(apps, schema_editor):
        Users = apps.get_model('Login', 'Users')
        user = Users(username = "admin", password = "password")
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insertData),
    ]

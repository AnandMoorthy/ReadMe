# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readme_api', '0008_auto_20170516_2145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='token',
            new_name='android_token',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='desktop_token',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='ios_token',
            field=models.CharField(default=0, max_length=100),
        ),
    ]

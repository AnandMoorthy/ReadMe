# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readme_api', '0004_auto_20170411_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='email_verified',
            field=models.CharField(default=b'no', max_length=10),
        ),
    ]

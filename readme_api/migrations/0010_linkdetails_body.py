# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readme_api', '0009_auto_20170517_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkdetails',
            name='body',
            field=models.TextField(default=b''),
        ),
    ]

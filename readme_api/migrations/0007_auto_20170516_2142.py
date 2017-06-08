# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readme_api', '0006_auto_20170515_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkdetails',
            name='description',
            field=models.TextField(default=b'None'),
        ),
        migrations.AddField(
            model_name='linkdetails',
            name='image',
            field=models.TextField(default=b'None'),
        ),
        migrations.AddField(
            model_name='linkdetails',
            name='title',
            field=models.TextField(default=b'None'),
        ),
    ]

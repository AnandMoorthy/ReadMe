# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readme_api', '0003_linkdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkdetails',
            name='body',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='linkdetails',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='linkdetails',
            name='image_link',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='linkdetails',
            name='title',
            field=models.TextField(default=None),
        ),
    ]

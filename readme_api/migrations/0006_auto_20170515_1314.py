# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readme_api', '0005_userdetails_email_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkdetails',
            name='body',
        ),
        migrations.RemoveField(
            model_name='linkdetails',
            name='description',
        ),
        migrations.RemoveField(
            model_name='linkdetails',
            name='image_link',
        ),
        migrations.RemoveField(
            model_name='linkdetails',
            name='title',
        ),
    ]

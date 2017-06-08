# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readme_api', '0007_auto_20170516_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkdetails',
            name='description',
            field=models.TextField(default=b'This is Description'),
        ),
        migrations.AlterField(
            model_name='linkdetails',
            name='image',
            field=models.TextField(default=b'http://tamil.thehindu.com/multimedia/dynamic/02444/high_court_madurai_2444480f.jpg'),
        ),
        migrations.AlterField(
            model_name='linkdetails',
            name='title',
            field=models.TextField(default=b'This is Title'),
        ),
    ]

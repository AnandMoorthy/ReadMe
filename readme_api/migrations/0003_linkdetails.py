# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readme_api', '0002_auto_20170311_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField()),
                ('user_id', models.IntegerField()),
                ('submitted_on', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'link_details',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-24 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardapp', '0003_auto_20191024_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.TextField(max_length=130),
        ),
    ]

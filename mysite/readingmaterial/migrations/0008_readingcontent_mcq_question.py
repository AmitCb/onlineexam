# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0013_auto_20160229_1616'),
        ('readingmaterial', '0007_auto_20160302_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingcontent',
            name='mcq_question',
            field=models.ManyToManyField(blank=True, null=True, to='qa1.Mcq_Question'),
        ),
    ]

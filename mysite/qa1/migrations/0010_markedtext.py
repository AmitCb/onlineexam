# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa1', '0009_auto_20160224_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marked_text', models.CharField(max_length=100)),
            ],
        ),
    ]
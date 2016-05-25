# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20160427_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription_plan',
            name='can_create_blog_tag',
            field=models.BooleanField(default=False, verbose_name='Can Create Blog Tag'),
        ),
        migrations.AlterField(
            model_name='subscription_plan',
            name='subscription_fee',
            field=models.IntegerField(default=0, verbose_name='Subscription Fee'),
        ),
    ]
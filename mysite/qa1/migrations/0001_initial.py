# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mcq_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice_a', models.CharField(max_length=200)),
                ('choice_b', models.CharField(max_length=200)),
                ('choice_c', models.CharField(max_length=200)),
                ('choice_d', models.CharField(max_length=200)),
                ('mcq_answer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_set_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='question_set',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='qa1.Topic'),
        ),
        migrations.AddField(
            model_name='mcq_question',
            name='question_set',
            field=models.ManyToManyField(blank=True, null=True, to='qa1.Question_Set'),
        ),
        migrations.AddField(
            model_name='mcq_question',
            name='subject_set',
            field=models.ManyToManyField(blank=True, null=True, to='qa1.Subject'),
        ),
        migrations.AddField(
            model_name='mcq_question',
            name='tag_set',
            field=models.ManyToManyField(blank=True, null=True, to='qa1.Tag'),
        ),
    ]
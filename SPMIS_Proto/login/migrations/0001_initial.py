# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='historyHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('searchQuery', models.TextField(blank=True, max_length=500)),
                ('dateAndTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='paperHolder',
            fields=[
                ('doi', models.TextField(max_length=100, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('papername', models.TextField(blank=True, max_length=500)),
                ('url', models.TextField(blank=True, max_length=500)),
                ('date', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='variable_holder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField()),
            ],
        ),
    ]

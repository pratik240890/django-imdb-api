# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-09 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedata', '0002_movie_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]

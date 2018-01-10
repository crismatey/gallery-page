# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting_title', models.CharField(max_length=200)),
                ('painting_image', models.ImageField(height_field=200, upload_to=None, width_field=200)),
                ('painting_text', models.CharField(max_length=200)),
                ('painting_year', models.IntegerField()),
                ('painting_style', models.CharField(choices=[('Acrylic', 'Acrylic'), ('Oil', 'Oil'), ('Watercolour', 'Watercolour'), ('Pencil', 'Pencil'), ('Other', 'Other')], default='Other', max_length=20)),
            ],
        ),
    ]
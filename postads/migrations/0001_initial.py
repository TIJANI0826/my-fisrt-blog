# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-17 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('gist', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('LAB', 'labor'), ('CAR', 'cars'), ('TRU', 'trucks'), ('WRI', 'writing')], max_length=3)),
                ('location', models.CharField(choices=[('BRO', 'Bronx'), ('BRK', 'Brooklyn'), ('QNS', 'Queens'), ('MAN', 'Manhattan'), ('STN', 'staten island')], max_length=3)),
                ('description', models.TextField(max_length=300)),
                ('expire', models.DateField()),
            ],
        ),
    ]
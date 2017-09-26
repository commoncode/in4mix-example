# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SparePart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('master_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spare_parts', to='parts.Product')),
                ('spare', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='parts.Product')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sparepart',
            unique_together=set([('master_product', 'spare')]),
        ),
    ]
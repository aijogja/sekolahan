# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sekolahapp', '0002_auto_20170830_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matapelajaran',
            name='jurusan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sekolahapp.Jurusan'),
        ),
    ]

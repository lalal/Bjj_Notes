# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_notes_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='note_category',
            field=models.CharField(max_length=100, null=True, verbose_name='Category'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoredFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(db_index=True, help_text='The file name of the stored file.', max_length=256, unique=True)),
                ('mime_type', models.CharField(blank=True, help_text='The MIME type of the stored file, if known.', max_length=128, null=True)),
                ('value', models.TextField(help_text='The encoded binary data in this file.')),
                ('size', models.IntegerField(db_index=True, help_text='The size of the stored file in bytes (the size of the actual file, not as it is stored).')),
                ('encoded_size', models.IntegerField(db_index=True, help_text='The size of the stored file in bytes, as stored.')),
                ('encoding', models.IntegerField(choices=[(0, 'None.'), (1, 'Base 64')])),
                ('gzipped', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]

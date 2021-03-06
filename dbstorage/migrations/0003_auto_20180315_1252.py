# Generated by Django 2.0.2 on 2018-03-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbstorage', '0002_storedfile_trusted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedfile',
            name='path',
            field=models.CharField(db_index=True, help_text='The file name of the stored file.', max_length=255, unique=True),
        ),
    ]

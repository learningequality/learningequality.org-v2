# Generated by Django 3.1.7 on 2021-04-14 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_customimage_file_hash'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BoardMembers',
            new_name='BoardMember',
        ),
    ]

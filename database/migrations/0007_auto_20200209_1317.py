# Generated by Django 2.0.13 on 2020-02-09 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20200209_0836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Constants',
            new_name='Field',
        ),
    ]
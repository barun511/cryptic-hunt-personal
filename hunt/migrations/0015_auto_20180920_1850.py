# Generated by Django 2.0.1 on 2018-09-20 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0014_appvariables'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppVariables',
            new_name='AppVariable',
        ),
    ]

# Generated by Django 2.0.2 on 2018-09-21 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0017_auto_20180921_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='time_of_level',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 2.0.1 on 2018-09-20 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0013_auto_20180919_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVariables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success_sign_up', models.CharField(max_length=200)),
            ],
        ),
    ]

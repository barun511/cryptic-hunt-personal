# Generated by Django 2.0.2 on 2018-09-19 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0012_auto_20180917_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='answer1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='level',
            name='answer2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='level',
            name='answer3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='level',
            name='level_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submitted_answer',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 3.0.7 on 2020-08-08 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0079_auto_20200808_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grading',
            name='description',
        ),
    ]
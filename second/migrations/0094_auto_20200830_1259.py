# Generated by Django 3.0.8 on 2020-08-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0093_auto_20200830_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='title',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(default='Course Name', max_length=10),
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-08 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0071_auto_20200808_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.FileField(blank=True, null=True, upload_to='syllabus/', verbose_name='Syllabus'),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0073_auto_20200808_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='assignments/', verbose_name=''),
        ),
    ]
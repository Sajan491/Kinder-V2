# Generated by Django 3.0.7 on 2020-07-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0052_auto_20200728_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='assignments/', verbose_name=''),
        ),
    ]

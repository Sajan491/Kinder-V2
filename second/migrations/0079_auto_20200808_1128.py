# Generated by Django 3.0.7 on 2020-08-08 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0078_auto_20200808_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

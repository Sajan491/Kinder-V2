# Generated by Django 3.0.8 on 2020-08-30 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0092_auto_20200830_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='title',
            field=models.CharField(default='Course Name', max_length=10),
        ),
    ]
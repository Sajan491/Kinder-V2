# Generated by Django 2.2.7 on 2020-01-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0012_food_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

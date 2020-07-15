# Generated by Django 2.2.7 on 2020-01-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0004_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('roll', models.IntegerField()),
                ('childid', models.IntegerField()),
                ('food', models.CharField(max_length=50)),
            ],
        ),
    ]

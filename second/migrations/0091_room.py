# Generated by Django 2.2.7 on 2020-09-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0090_auto_20200828_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
    ]
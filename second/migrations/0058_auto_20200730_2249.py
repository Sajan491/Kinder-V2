# Generated by Django 2.2.7 on 2020-07-30 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0057_auto_20200730_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='c',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='second.Course'),
        ),
    ]

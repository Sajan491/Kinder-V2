# Generated by Django 2.2.7 on 2020-01-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200108_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_parents',
            name='UserType',
            field=models.CharField(default='parent', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_teachers',
            name='UserType',
            field=models.CharField(default='teacher', max_length=20),
            preserve_default=False,
        ),
    ]

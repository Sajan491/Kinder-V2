# Generated by Django 3.0.7 on 2020-07-28 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0065_auto_20200728_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submissions',
            old_name='title',
            new_name='assignment',
        ),
    ]
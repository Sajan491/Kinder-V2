# Generated by Django 2.2.7 on 2020-01-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200108_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_parents',
            old_name='ChildName',
            new_name='school',
        ),
        migrations.AddField(
            model_name='user_teachers',
            name='school',
            field=models.CharField(default='school', max_length=200),
            preserve_default=False,
        ),
    ]
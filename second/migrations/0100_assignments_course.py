# Generated by Django 3.0.7 on 2020-09-29 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0099_merge_20200929_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='second.Course'),
        ),
    ]
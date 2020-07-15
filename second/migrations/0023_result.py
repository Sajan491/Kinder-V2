# Generated by Django 3.0.2 on 2020-02-07 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0022_auto_20200204_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.PositiveIntegerField()),
                ('subject2', models.PositiveIntegerField()),
                ('subject3', models.PositiveIntegerField()),
                ('subject4', models.PositiveIntegerField()),
                ('remarks', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.Attendance')),
            ],
        ),
    ]
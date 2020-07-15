# Generated by Django 3.0 on 2020-02-04 14:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0020_auto_20200203_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absentday',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='absentday',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.Attendance'),
        ),
        migrations.CreateModel(
            name='Presentday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.Attendance')),
            ],
        ),
    ]
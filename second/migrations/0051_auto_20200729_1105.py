# Generated by Django 2.2.7 on 2020-07-29 05:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0050_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='announcement',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_plan',
            field=models.FileField(null=True, upload_to='course_plan/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='course',
            name='syllabus',
            field=models.FileField(null=True, upload_to='syllabus/', verbose_name=''),
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial', models.FileField(null=True, upload_to='tutorial/', verbose_name='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.Course')),
            ],
            options={
                'ordering': ['date_posted'],
            },
        ),
    ]
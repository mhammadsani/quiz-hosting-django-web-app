# Generated by Django 4.2.4 on 2023-09-23 23:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
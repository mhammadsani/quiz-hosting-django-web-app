# Generated by Django 4.2.5 on 2023-09-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_management', '0002_alter_quiz_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.JSONField()),
                ('is_public', models.BooleanField(default=False)),
                ('question_marks', models.IntegerField(default=1)),
                ('quiz', models.ManyToManyField(to='quiz_management.quiz')),
            ],
        ),
    ]

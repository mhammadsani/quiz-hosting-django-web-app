# Generated by Django 4.2.5 on 2023-10-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_attempter_management', '0004_alter_mark_options_rename_marks_mark_obtained_mark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mark',
            options={'ordering': ['-marks']},
        ),
        migrations.RenameField(
            model_name='mark',
            old_name='obtained_mark',
            new_name='marks',
        ),
    ]

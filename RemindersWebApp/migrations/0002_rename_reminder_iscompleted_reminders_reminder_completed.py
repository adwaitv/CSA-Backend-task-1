# Generated by Django 3.2.12 on 2022-03-05 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RemindersWebApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminders',
            old_name='reminder_iscompleted',
            new_name='reminder_Completed',
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-05 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder_name', models.CharField(max_length=200)),
                ('reminder_time', models.DateTimeField(blank=True, null=True)),
                ('reminder_iscompleted', models.BooleanField(default=False)),
            ],
        ),
    ]

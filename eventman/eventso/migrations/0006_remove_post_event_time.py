# Generated by Django 3.2.3 on 2021-05-26 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventso', '0005_auto_20210526_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='event_time',
        ),
    ]
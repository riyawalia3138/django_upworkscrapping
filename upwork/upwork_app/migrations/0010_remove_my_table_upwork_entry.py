# Generated by Django 3.2 on 2023-08-03 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upwork_app', '0009_remove_dataa_my_table_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_table',
            name='upwork_entry',
        ),
    ]

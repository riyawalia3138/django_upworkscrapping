# Generated by Django 3.2 on 2023-08-02 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upwork_app', '0005_upwork_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataa',
            name='my_table_entry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='upwork_app.my_table'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='my_table',
            name='upwork_entry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='upwork_app.upwork'),
            preserve_default=False,
        ),
    ]

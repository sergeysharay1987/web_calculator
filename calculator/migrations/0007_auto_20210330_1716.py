# Generated by Django 3.1.4 on 2021-03-30 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_auto_20210330_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exp',
            old_name='created_at',
            new_name='date',
        ),
    ]
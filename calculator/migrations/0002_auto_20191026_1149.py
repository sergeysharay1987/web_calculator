# Generated by Django 2.2.4 on 2019-10-26 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exp',
            old_name='exprassion',
            new_name='exp',
        ),
    ]

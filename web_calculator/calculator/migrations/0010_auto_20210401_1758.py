# Generated by Django 3.1.4 on 2021-04-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0009_auto_20210401_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expression',
            name='result_of_expression',
        ),
        migrations.AddField(
            model_name='expression',
            name='result',
            field=models.CharField(blank=True, max_length=150, verbose_name='result'),
        ),
    ]

# Generated by Django 2.2.12 on 2020-11-02 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('effortloop', '0008_auto_20201102_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='redistribute_eff',
        ),
    ]

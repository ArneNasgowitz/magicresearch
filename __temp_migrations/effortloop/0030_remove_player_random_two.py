# Generated by Django 2.2.12 on 2020-11-11 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('effortloop', '0029_player_performance_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='random_two',
        ),
    ]

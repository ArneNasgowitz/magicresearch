# Generated by Django 2.2.12 on 2020-11-09 10:03

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0015_auto_20201109_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='performance_guess',
            field=otree.db.models.IntegerField(choices=[[1, '10 - Highest score'], [2, '9'], [3, '8'], [4, '7'], [5, '6'], [6, '5'], [7, '4'], [8, '3'], [9, '2'], [10, '1 - Lowest score']], null=True, verbose_name=''),
        ),
    ]
# Generated by Django 2.2.12 on 2020-11-05 10:23

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0011_auto_20201104_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='performance_guess',
            field=otree.db.models.IntegerField(choices=[[1, '1 - Highest amount'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10 - Lowest amount']], null=True),
        ),
    ]

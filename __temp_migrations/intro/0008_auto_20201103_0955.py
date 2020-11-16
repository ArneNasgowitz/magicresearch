# Generated by Django 2.2.12 on 2020-11-03 08:55

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0007_auto_20201103_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='performance_guess',
            field=otree.db.models.IntegerField(choices=[[1, '1 - Lowest amount'], [2, '2'], [3, '3'], [4, '4'], [5, '5 - Average amount'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10 - Highest amount']], null=True),
        ),
    ]

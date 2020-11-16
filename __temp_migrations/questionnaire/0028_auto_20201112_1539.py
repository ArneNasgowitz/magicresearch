# Generated by Django 2.2.12 on 2020-11-12 14:39

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0027_auto_20201112_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='pilot_eff',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Hola2'),
        ),
        migrations.AlterField(
            model_name='player',
            name='pilot_inv',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Hola'),
        ),
    ]
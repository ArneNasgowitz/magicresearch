# Generated by Django 2.2.12 on 2020-11-05 12:32

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0009_auto_20201104_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='education',
            field=otree.db.models.IntegerField(choices=[[1, 'No education'], [2, 'Primary education'], [3, 'Secondary education'], [4, 'Tertiary education or above']], null=True, verbose_name='What is the highest level of education you completed?'),
        ),
    ]

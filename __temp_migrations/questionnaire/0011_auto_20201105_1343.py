# Generated by Django 2.2.12 on 2020-11-05 12:43

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_auto_20201105_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='health',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='On a scale of 1-5, 1 being very bad and 5 being very good. How is your health in general?'),
        ),
    ]

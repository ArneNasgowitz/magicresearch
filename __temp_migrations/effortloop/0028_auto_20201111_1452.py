# Generated by Django 2.2.12 on 2020-11-11 13:52

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('effortloop', '0027_auto_20201109_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='payoff_effort',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='payoff_luck',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='random_one',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='random_two',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]

# Generated by Django 2.2.12 on 2020-11-03 09:04

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('effortloop', '0015_player_guess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='treat_2_ctrl',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Remember the essay that you wrote some moments ago about a typical day in your life. Is the day that you described a typcial day in your life?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='treat_2_rel',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Remember the essay that you wrote some moments ago about god and religion.Did you attend any religious meeting during the last week, such as a mass?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='treat_2_wc',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Remember the essay that you wrote some moments ago about witchcraft. Did you exprience any situation related to what you described during the last week?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='treat_3_ctrl',
            field=otree.db.models.IntegerField(choices=[[1, 'No one'], [2, 'Very few'], [3, 'A fair amount'], [4, 'Most people'], [5, 'everyone']], null=True, verbose_name='Remember the essay that you wrote some moments ago about a typical day in your life. How many people in your village do you think have similar days?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='treat_3_rel',
            field=otree.db.models.IntegerField(choices=[[1, 'No one'], [2, 'Very few'], [3, 'A fair amount'], [4, 'Most people'], [5, 'everyone']], null=True, verbose_name='Remember the essay that you wrote some moments ago about god and religion. How many people in your village have similar views on religion as you?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='treat_3_wc',
            field=otree.db.models.IntegerField(choices=[[1, 'No one'], [2, 'Very few'], [3, 'A fair amount'], [4, 'Most people'], [5, 'everyone']], null=True, verbose_name='Remember the essay that you wrote some moments ago about witchcraft. How many people in your village think similarly about witchcraft as you?'),
        ),
    ]

# Generated by Django 2.2.12 on 2020-11-12 14:13

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0019_player_performance_tr'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='att_effort',
            field=otree.db.models.BooleanField(choices=[[True, 'higher'], [False, 'lower']], null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='player',
            name='att_invest1',
            field=otree.db.models.BooleanField(choices=[[True, '8'], [False, '2']], null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='player',
            name='att_invest2',
            field=otree.db.models.BooleanField(choices=[[True, '2'], [False, '8']], null=True, verbose_name=''),
        ),
    ]

# Generated by Django 2.2.12 on 2020-11-05 13:02

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0012_auto_20201105_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='nb_correct_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='nb_display1_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='nb_display2_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='nb_display3_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='nb_display4_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='nb_inserted_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='payoff_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='round_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]

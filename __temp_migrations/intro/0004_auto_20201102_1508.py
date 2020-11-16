# Generated by Django 2.2.12 on 2020-11-02 14:08

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0003_auto_20201102_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='q1',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Afraid'),
        ),
        migrations.AddField(
            model_name='player',
            name='q10',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Happy'),
        ),
        migrations.AddField(
            model_name='player',
            name='q11',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Alert'),
        ),
        migrations.AddField(
            model_name='player',
            name='q12',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Nervous'),
        ),
        migrations.AddField(
            model_name='player',
            name='q13',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Timid'),
        ),
        migrations.AddField(
            model_name='player',
            name='q14',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Hostile'),
        ),
        migrations.AddField(
            model_name='player',
            name='q15',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Enthusiastic'),
        ),
        migrations.AddField(
            model_name='player',
            name='q16',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Blameworthy'),
        ),
        migrations.AddField(
            model_name='player',
            name='q17',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Guilty'),
        ),
        migrations.AddField(
            model_name='player',
            name='q18',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Confident'),
        ),
        migrations.AddField(
            model_name='player',
            name='q19',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Hostile'),
        ),
        migrations.AddField(
            model_name='player',
            name='q2',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='player',
            name='q20',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='lonely'),
        ),
        migrations.AddField(
            model_name='player',
            name='q3',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Nervous'),
        ),
        migrations.AddField(
            model_name='player',
            name='q4',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Calm'),
        ),
        migrations.AddField(
            model_name='player',
            name='q5',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Surprised'),
        ),
        migrations.AddField(
            model_name='player',
            name='q6',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Scared'),
        ),
        migrations.AddField(
            model_name='player',
            name='q7',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Inspired'),
        ),
        migrations.AddField(
            model_name='player',
            name='q8',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Energetic'),
        ),
        migrations.AddField(
            model_name='player',
            name='q9',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Strong'),
        ),
    ]

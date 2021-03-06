# Generated by Django 2.2.12 on 2020-11-03 12:24

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('effortloop', '0019_auto_20201103_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='q10',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Irritable'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q11',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Determined'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q12',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Scared'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q13',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Proud'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q14',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Alone'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q15',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Strong'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q16',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Joyful'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q17',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Tired'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q18',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Fearless'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q20',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Guilty'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q5',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Happy'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q6',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Attentive'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q7',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Nervous'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q8',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Enthusiastic'),
        ),
        migrations.AlterField(
            model_name='player',
            name='q9',
            field=otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Ashamed'),
        ),
    ]

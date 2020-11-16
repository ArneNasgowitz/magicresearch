# Generated by Django 2.2.12 on 2020-11-12 14:31

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0020_auto_20201112_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='att_invest1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='att_invest2',
        ),
        migrations.AddField(
            model_name='player',
            name='att_invest',
            field=otree.db.models.BooleanField(choices=[[True, '2 if unlucky and 8 if lucky'], [False, '4 if unlucky and 4 if lucky']], null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='att_effort',
            field=otree.db.models.BooleanField(choices=[[True, 'It will be higher'], [False, 'It will be lower']], null=True, verbose_name=''),
        ),
    ]
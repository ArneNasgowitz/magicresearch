# Generated by Django 2.2.12 on 2020-11-11 14:45

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0018_remove_player_performance_tr'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='performance_tr',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
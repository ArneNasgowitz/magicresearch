# Generated by Django 2.2.12 on 2020-11-02 15:00

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('effortloop', '0006_auto_20201102_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='redistribute_eff',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]

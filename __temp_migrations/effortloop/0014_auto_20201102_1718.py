# Generated by Django 2.2.12 on 2020-11-02 16:18

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('effortloop', '0013_auto_20201102_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='redistribute_luck1',
            field=otree.db.models.IntegerField(null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='redistribute_luck2',
            field=otree.db.models.IntegerField(null=True, verbose_name=''),
        ),
    ]

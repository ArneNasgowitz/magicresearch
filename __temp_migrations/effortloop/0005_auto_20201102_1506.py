# Generated by Django 2.2.12 on 2020-11-02 14:06

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('effortloop', '0004_auto_20201102_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='treat_2_rel',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Remember the essay that you wrote some moments ago. When was the last time you thought about god or relgion?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='treat_3_ctrl',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Remember the essay that you wrote some moments ago. How often do you experinece such a typical day?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='treat_3_rel',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Remember the essay that you wrote some moments ago. How often do you think about god and/or religion?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='treat_3_wc',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Remember the essay that you wrote some moments ago. How often do you experience such a situation?'),
        ),
    ]

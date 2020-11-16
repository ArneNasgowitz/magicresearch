# Generated by Django 2.2.12 on 2020-11-05 12:52

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0013_auto_20201105_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='language',
            field=otree.db.models.IntegerField(choices=[[1, 'English'], [2, 'Zulu'], [3, 'Xhosa'], [4, 'Afrikaans'], [5, 'Sepedi'], [6, 'Tswana'], [7, 'Sotho']], null=True, verbose_name='What is your first language?'),
        ),
    ]
# Generated by Django 2.2.12 on 2020-11-06 12:02

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0016_auto_20201105_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='check_one',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='Please briefly speculate about what this study is about (one word is enough).'),
        ),
    ]

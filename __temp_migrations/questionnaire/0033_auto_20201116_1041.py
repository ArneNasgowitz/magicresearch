# Generated by Django 2.2.12 on 2020-11-16 09:41

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0032_auto_20201116_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='witchcraft_int',
            field=otree.db.models.IntegerField(choices=[[1, 'Very weak'], [2, 'Weak'], [3, 'Moderate'], [4, 'Strong'], [5, 'Very strong']], null=True, verbose_name="How strongly do you believe in witchcraft? (Leave this blank, when you answered 'No' to the previous question)"),
        ),
        migrations.AlterField(
            model_name='player',
            name='religion_int',
            field=otree.db.models.IntegerField(blank=True, choices=[[1, 'Very weak'], [2, 'Weak'], [3, 'Moderate'], [4, 'Strong'], [5, 'Very strong']], null=True, verbose_name="How strongly do you believe in this religion? (Leave this blank, when you answered 'No' to the previous question)"),
        ),
        migrations.AlterField(
            model_name='player',
            name='witchcraft',
            field=otree.db.models.BooleanField(choices=[[False, 'No'], [True, 'Yes']], null=True, verbose_name='Do you believe in witchcraft, that is, do you believe witchcraft is possible'),
        ),
    ]
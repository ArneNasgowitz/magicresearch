from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

# Socio-demographics

    age = models.IntegerField(
        label="What is your age?"
    )
    gender = models.BooleanField(
        label="What is your gender?",
        choices=[
            [False, 'Female'],
            [True, 'Male']
        ]
    )
    # Fine-tune this with the SA education system
    education = models.IntegerField(
        label="What is the highest level of education you completed?",
        choices=[
            [1, 'No education'],
            [2, 'Primary education'],
            [3, 'Secondary education'],
            [4, 'Tertiary education or above'],
        ]
    )
    religion = models.IntegerField(
        label="What comes closest to describing your religious orientation",
        choices=[
            [1, 'Christian - African Independent Church'],
            [2, 'Christian - Pentecoastal'],
            [3, 'Christian - Catholic Church'],
            [4, 'Christian - Other'],
            [5, 'Traditional African religion'],
            [6, 'Islam'],
            [7, 'Jewish'],
            [8, 'Other religion'],
            [9, 'No religion'],
            # tbc
        ]
    )
    religion_int = models.IntegerField(
        label="How strongly do you believe in this religion? (Leave this blank, when you answered 'No' to the previous question)",
        choices=[
            [1,'Very weak'],
            [2,'Weak'],
            [3,'Moderate'],
            [4,'Strong'],
            [5,'Very strong'],
        ],
        blank=True,
        widget=widgets.RadioSelectHorizontal
    )
    witchcraft = models.BooleanField(
        label="Do you believe in witchcraft, that is, do you believe witchcraft is possible?",
        choices=[
            [False, 'No'],
            [True, 'Yes']
        ]
    )
    # This is taken from Lowes and Nunn. It is possible that the treatment shifts beliefs slightly,
    # so probably compress in analysis
    witchcraft_int = models.IntegerField(
        label="How strongly do you believe in witchcraft? (Leave this blank, when you answered 'No' to the previous question)",
        choices=[
            [1,'Very weak'],
            [2,'Weak'],
            [3,'Moderate'],
            [4,'Strong'],
            [5,'Very strong']
        ],
        blank=True,
        widget=widgets.RadioSelectHorizontal
    )
    nationality = models.BooleanField(
        label="What is your nationality?",
        choices=[
            [False, 'Other'],
            [True, 'South Africa'],
        ]
    )
    language = models.IntegerField(
        label="What is your first language?",
        choices=[
            [1, 'English'],
            [2, 'Zulu'],
            [3, 'Xhosa'],
            [4, 'Afrikaans'],
            [5, 'Sepedi'],
            [6, 'Tswana'],
            [7, 'Sotho'],
            [8, 'Other'],
        ]
    )
    ethnicity_strength = models.StringField(
        label="How important is your ethnicity to you?"
    )
    rural = models.BooleanField(
        label="Do you live in an urban (city) or a rural area (village, town)?",
        choices=[
            [True, 'Rural'],
            [False, 'Urban']
        ]
    )
    marstat = models.IntegerField(
        label="What is your marital status?",
        choices=[
            [1, 'Single'],
            [2, 'Couple'],
            [3, 'Married'],
            [4, 'Separated/Divorced'],
            [5, 'Widow/Widower'],
        ]
    )
    employment = models.IntegerField(
        label="What best describes your employment status?",
        choices=[
            [1, 'Unemployed'],
            [2, 'Student'],
            [3, 'Self-employed'],
            [4, 'Wage-employed'],
            [5, 'Retired']
        ]
    )
    occupation = models.StringField(
        label="What is your current occupation? (If you currently don't have an occupation, enter your last occupation. "
              "If you never had a occupation, leave this field blank.)",
        blank=True
    )
    income = models.IntegerField(
        label="In which range is your household's monthly income (in Rand)?",
        choices=[
            [1, 'Below 2.000'],
            [2, '2.000 - 4.000'],
            [3, '4.000 - 8.000'],
            [4, '8.000 - 12.000'],
            [5, '12.000 - 20.000'],
            [6, 'More than 20.000']
        ]
    )

# Others (Happiness, maybe shocks)
    # Cantril ladder
    happy = models.IntegerField(
        label="Imagine a ladder with steps numbered from one at the bottom to ten at the top. "
              "The top of the ladder represents the best possible life for you and "
              "the bottom of the ladder represents the worst possible life for you. "
              "On which step of the ladder do you feel you personally stand at the present time?",
        choices=[1,2,3,4,5,6,7,8,9,10],
        widget=widgets.RadioSelectHorizontal
    )

    health = models.IntegerField(
        label="On a scale of 1-5, 1 being very bad and 5 being very good. How is your health in general?",
        choices=[1,2,3,4,5],
        widget=widgets.RadioSelectHorizontal,
    )

    trust = models.BooleanField(
        label="Generally speaking, would you say that most people can be trusted or that you need to be "
              "very careful in dealing with people?",
        choices=[
            [True, 'Most people can be trusted'],
            [False, 'You can`t be too careful']
        ]    )

# Experiment-specific feedback and checks
    check_one=models.StringField(
        label="What do you think this study was about? A short answer, such as one word, is enough."
    )
    check_two = models.BooleanField(
        label="Have you read about a study that does similar tasks as the ones you completed today?",
        choices=[
            [True, 'Yes'],
            [False, 'No']
        ]
    )

    check_three = models.StringField(
        label="Has there been anything that you do not understand or find odd about this study?",
    )
    feedback = models.LongStringField(
        label="Do you have any oher feedback about the study?",
        blank=True,
    )
# Pilot-specifics
    pilot_inv = models.IntegerField(
        label="Investment task",
        choices=[1,2,3,4,5],
        widget=widgets.RadioSelectHorizontal,
    )
    pilot_eff = models.IntegerField(
        label="Effort task",
        choices=[1,2,3,4,5],
        widget=widgets.RadioSelectHorizontal,
    )
    pilot_redis = models.IntegerField(
        label="Redistribution task",
        choices=[1,2,3,4,5],
        widget=widgets.RadioSelectHorizontal,
    )
    pilot_overall = models.IntegerField(
        label="Whole study",
        choices=[1,2,3,4,5],
        widget=widgets.RadioSelectHorizontal,
    )
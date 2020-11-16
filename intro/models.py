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
    name_in_url = 'Introduction'
    players_per_group = None
    num_rounds = 15
    payment_per_seq  =1

    INTS_T0 = [
    [111101111, 110101010, 110111101, 110011100, 11],
    [100111010, 111110000, 100111000, 111100000, 18],
    [100001010, 111111111, 111100010, 110110110, 13],
    [100110000, 110110011, 100111010, 111000001, 18],
    [100001000, 101010101, 110111011, 110110111, 15],
    [110011000, 101010101, 111100011, 100000000, 20 ],
    [111000111, 110000011, 100000001, 111111111, 15 ],
    [100110100, 100100100, 101101001, 111011010, 18 ],
    [100000001, 110001101, 111010101, 100011000, 20 ],
    [100010000, 111110110, 101111010, 101010011, 16 ],
    [111111110, 101011111, 110011111, 110011110, 8 ],
    [101010101, 110101011, 101010101, 110101011, 14 ],
    [101110100, 101100010, 111001110, 100000110, 18 ],
    [110110111, 100100010, 100010010, 100000100, 21 ],
    [100100010, 101110010, 111110001, 101000110, 18 ],
    ]


class Subsession(BaseSubsession):

    # 1-Control,2-WC,3-Religion, 4&5 with redistribution
    def creating_session(self):
        import itertools
        treatments = itertools.cycle(['one', 'two', 'three', 'four', 'five'])
         # Randomize the players into treaments ...
        if self.round_number == 1:
            for p in self.get_players():
                # p.participant.vars['treatment'] = next(treatments) # Saves Assignment - ok
                treatment = next(treatments)
                p.participant.vars['treatment'] = treatment # Stored in participant
                p.treatment = treatment # stored as variable output
                # Does this work? -> TEST!
                if p.treatment == 'one' or p.treatment == 'two' or p.treatment == 'three':
                    p.redis = 0
                    p.participant.vars['redis'] = p.redis
                else:
                    p.redis = 1
                    p.participant.vars['redis'] = p.redis # Should work, but only saved in one player-session

        for p in self.get_players():
            p.nb_display1_tr = Constants.INTS_T0[self.round_number - 1][0]
            p.nb_display2_tr = Constants.INTS_T0[self.round_number - 1][1]
            p.nb_display3_tr = Constants.INTS_T0[self.round_number - 1][2]
            p.nb_display4_tr = Constants.INTS_T0[self.round_number - 1][3]
            p.nb_correct_tr = Constants.INTS_T0[self.round_number - 1][4]
            # This can be used to give the current the player is in. Enough as this is within subsession (no transfer)
            p.round_tr = self.round_number


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    round_tr = models.IntegerField()
    treatment = models.StringField()
    performance_tr = models.IntegerField()

    nb_inserted_tr =models.IntegerField()
    nb_correct_tr = models.IntegerField()
    nb_display1_tr = models.IntegerField()
    nb_display2_tr = models.IntegerField()
    nb_display3_tr = models.IntegerField()
    nb_display4_tr = models.IntegerField()

    redis=models.BooleanField()
    performance_guess = models.IntegerField(
        label='',
        choices=[
            [1,'10 - Highest score'],
            [2,'9'],
            [3,'8'],
            [4,'7'],
            [5,'6'],
            [6,'5'],
            [7,'4'],
            [8,'3'],
            [9,'2'],
            [10,'1 - Lowest score'],
        ],
            widget=widgets.RadioSelect
    )

    invest_cash_tr = models.IntegerField(
        choices=[0,1,2,3,4],
        label=""
    )
    invest_inv_tr = models.IntegerField(
        choices=[0,1,2,3,4],
        label=""
    )
    att_invest = models.BooleanField(
        label="",
        choices=[
            [True, '2 if unlucky and 8 if lucky'],
            [False, '4 if unlucky and 4 if lucky']
        ]
    )
    att_effort = models.BooleanField(
        label="",
        choices=[
            [True, 'It will be higher'],
            [False, 'It will be lower']
        ]
    )
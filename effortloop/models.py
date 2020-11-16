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
    name_in_url = 'Tasks'
    players_per_group = None
    num_rounds = 15
    payment_per_seq  = 1

    INTS_T1 = [
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

    def creating_session(self):
        for p in self.get_players():
            p.nb_display1 = Constants.INTS_T1[self.round_number - 1][0]
            p.nb_display2 = Constants.INTS_T1[self.round_number - 1][1]
            p.nb_display3 = Constants.INTS_T1[self.round_number - 1][2]
            p.nb_display4 = Constants.INTS_T1[self.round_number - 1][3]
            p.nb_correct = Constants.INTS_T1[self.round_number - 1][4]
            # This can be used to give the current the player is in. Enough as this is within subsession (no transfer)
            p.round = self.round_number
            import random
            p.random_one = random.choice([0,1])
            p.participant.vars['random_one'] = p.random_one

class Group(BaseGroup):
    pass


class Player(BasePlayer):
# Payoffs: There are two potential payoffs, one of them will be drawn at random to be relevant and
# assigned to the pre-existing variable payoff
    payoff_luck = models.IntegerField()
    payoff_effort = models.IntegerField()
    random_one = models.BooleanField()

    performance_main = models.IntegerField()

    round = models.IntegerField()
# Treatments
    treat_main_wc = models.LongStringField(
        label=""
    )
    treat_main_ctrl = models.LongStringField(
        label=""
    )
    treat_main_rel = models.LongStringField(
        label=""
    )
    treat_2_ctrl = models.BooleanField(
        label="Remember the essay that you wrote some moments ago about a typical day in your life. "
              "Think about it carefully: Is the day that you described a typical day in your life?"
    )
    treat_2_wc = models.BooleanField(
        label="Remember the essay that you wrote some moments ago about witchcraft. "
              "Think about it carefully: Did you experience any situation related to what you described during the last week?"
    )
    treat_2_rel = models.BooleanField(
        label="Remember the essay that you wrote some moments ago about God and religion. "
              "Think about it carefully: Did you attend any religious meeting during the last week?"
    )
    treat_3_ctrl = models.IntegerField(
        choices=[ # Alternative: Out of 100 ppl, ?
            [1, 'No one'],
            [2, 'Very few'],
            [3, 'A fair number of people'],
            [4, 'Most people'],
            [5, 'Everyone']
        ],
        label="Remember the essay that you wrote some moments ago about a typical day in your life. "
              "Think about it carefully: How many people in your village do you think have similar days?"
    )
    treat_3_wc = models.IntegerField(
        choices=[
            [1, 'No one'],
            [2, 'Very few'],
            [3, 'A fair number of people'],
            [4, 'Most people'],
            [5, 'Everyone']
        ],
        label="Remember the essay that you wrote some moments ago about witchcraft. "
              "Think about it carefully: How many people in your village think similarly about witchcraft as you?"
    )
    treat_3_rel = models.IntegerField(
        choices=[
            [1, 'No one'],
            [2, 'Very few'],
            [3, 'A fair number of people'],
            [4, 'Most people'],
            [5, 'Everyone']
        ],
        label="Remember the essay that you wrote some moments ago about God and religion. "
              "Think about it carefully: How many people in your country have similar views on religion as you?"
    )

# Redistribution

    redistribute_luck1=models.IntegerField(
        min=0,
        max=6,
        label=""
    )
    redistribute_luck2=models.IntegerField(
        min=0,
        max=6,
        label=""
    )

    redistribute_eff1=models.IntegerField(
        min=0,
        max=6,
        label=""
    )
    redistribute_eff2=models.IntegerField(
        min=0,
        max=6,
        label=""
    )
# Effort
    nb_inserted =models.IntegerField()
    nb_correct = models.IntegerField()
    nb_display1 = models.IntegerField()
    nb_display2 = models.IntegerField()
    nb_display3 = models.IntegerField()
    nb_display4 = models.IntegerField()

    invest = models.IntegerField(
        label="How much do you want to invest",
        choices=[0,1,2,3,4],
        widget=widgets.RadioSelectHorizontal,
    )
# Investment
    invest_cash_main = models.IntegerField(
        choices=[0,1,2,3,4],
        label="Cash Account"
    )
    invest_inv_main = models.IntegerField(
        choices=[0,1,2,3,4],
        label="Investment Account"
    )

# PANAS
    def panas(label):
        return models.IntegerField(
            choices=[1, 2, 3, 4, 5],
            label=label,
            widget=widgets.RadioSelectHorizontal,
        )

    q1 = panas('Afraid')
    q2 = panas('Calm')
    q3 = panas('Sad')
    q4 = panas('Angry')
    q5 = panas('Happy')
    q6 = panas('Attentive')
    q7 = panas('Nervous')
    q8 = panas('Enthusiastic')
    q9 = panas('Ashamed')
    q10 = panas('Irritable')
    q11 = panas('Determined')
    q12 = panas('Scared')
    q13 = panas('Proud')
    q14 = panas('Alone')
    q15 = panas('Strong')
    q16 = panas('Joyful')
    q17 = panas('Tired')
    q18 = panas('Fearless')
    q19 = panas('Hostile')
    q20 = panas('Guilty')

    guess = models.IntegerField()
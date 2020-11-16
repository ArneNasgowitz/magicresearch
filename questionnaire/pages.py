from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Qst1(Page):
    form_model = 'player'
    form_fields = ['age','gender','education','nationality','language','religion','religion_int',
                   'witchcraft','witchcraft_int','marstat','employment','occupation','income','rural']

class Qst2(Page):
    form_model = 'player'
    form_fields = ['happy', 'health', 'trust']

class Qst3(Page):
    form_model = 'player'
    form_fields = ['check_one','feedback','pilot_eff','pilot_inv','pilot_redis','pilot_overall']

class FinalPage(Page):
    pass

# PANAS is first, but takes most time
page_sequence = [Qst1, Qst2, Qst3, FinalPage]

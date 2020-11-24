from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):

    def is_displayed(self):
        return self.round_number == 1

class Training(Page):
    def is_displayed(self):
        return self.round_number == 1

class Investment_tr(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields =['invest_cash_tr','invest_inv_tr']

    def error_message(self,values):
        print('value is', values)
        if values['invest_cash_tr'] + values['invest_inv_tr'] != 4: # Might need to change that
            return 'The sum has to be 4 points'

class Effort_intro_tr(Page):
    def is_displayed(self):
        return self.round_number == 1

    # define timer. Has to be moved to the page before the effort task
    def before_next_page(self):
        import time
        self.participant.vars['expiry_tr'] = time.time() + 45
        self.participant.vars['performance_tr'] = 0

class Effort_tr(Page):

    form_model = "player"
    form_fields = ['nb_inserted_tr']

    def is_displayed(self): # Not in last round(s) (display other pages there)
        return self.round_number < Constants.num_rounds

    timer_text = 'time left to complete this task'

    def get_timeout_seconds(self): # Update time left
        import time
        return self.participant.vars['expiry_tr'] - time.time()

    def is_displayed(self): # If not, all remaining pages are displayed at once
        return self.get_timeout_seconds() > 3 # Combine with and?

    def before_next_page(self):
        if self.player.nb_inserted_tr == self.player.nb_correct_tr:
            self.participant.vars['performance_tr'] += Constants.payment_per_seq

class Effort_feedback(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields =['performance_guess']

    def before_next_page(self):
        self.participant.vars['guess']=self.player.performance_guess
        self.player.performance_tr = self.participant.vars['performance_tr']



class End(Page):

    form_model = 'player'
    form_fields =['att_effort','att_invest']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds  and self.participant.vars['redis'] == 0

page_sequence = [Intro, Training, Investment_tr, Effort_intro_tr, Effort_tr, Effort_feedback, End]

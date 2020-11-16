from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# TREATMENTS
############
class Treatment_main_ctrl_intro(Page):

    def is_displayed(self):
        return self.round_number == 1 and (self.participant.vars['treatment'] == 'one' or self.participant.vars['treatment'] == 'four')
        # and XXX (see otree template)

class Treatment_main_ctrl(Page):

    form_model = "player"
    form_fields = ['treat_main_ctrl']
    timeout_seconds = 90
    timer_text = 'Time left to complete the essay'

    def is_displayed(self):
        return self.round_number == 1 and (self.participant.vars['treatment'] == 'one' or self.participant.vars['treatment'] == 'four')
        # and XXX (see otree template)

class Treatment_main_wc_intro(Page):

    def is_displayed(self):
        return self.round_number == 1 and (self.participant.vars['treatment'] == 'two' or self.participant.vars['treatment'] == 'five')

class Treatment_main_wc(Page):

    form_model = "player"
    form_fields = ['treat_main_wc']
    timeout_seconds = 90
    timer_text = 'Time left to complete the essay'

    def is_displayed(self):
        return self.round_number == 1 and (self.participant.vars['treatment'] == 'two' or self.participant.vars['treatment'] == 'five')

class Treatment_main_rel_intro(Page):

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'three'

class Treatment_main_rel(Page):

    form_model = "player"
    form_fields = ['treat_main_rel']
    timeout_seconds = 90
    timer_text = 'Time left to complete the essay'

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'three'

# REDISTRIBUTION
################

class Redistribution_1(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.guess = self.participant.vars['guess']

class Redistribution_2(Page):

    form_model = "player"
    form_fields = ['redistribute_eff1','redistribute_eff2']

    def is_displayed(self):
        return self.round_number == 1

    def error_message(self,values):
        print('value is', values)
        if values['redistribute_eff1'] + values['redistribute_eff2'] != 6: # Might need to change that
            return 'The numbers must add up to 6'

class Redistribution_3(Page):

    form_model = "player"
    form_fields = ['redistribute_luck1','redistribute_luck2' ]

    def is_displayed(self):
        return self.round_number == 1

    def error_message(self,values):
        print('value is', values)
        if values['redistribute_luck1'] + values['redistribute_luck2'] != 6: # Might need to change that
            return 'The numbers must add up to 6'

class Redistribution_4(Page):

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['redis'] == 0

class Redistribution_4_red(Page):

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['redis'] == 1

class Investment(Page):

    form_model = "player"
    form_fields = ['invest_cash_main','invest_inv_main']

    # If before effort task. If after, change to == Constants.num_rounds - 1
    def is_displayed(self):
        return self.round_number ==  1

    def error_message(self,values):
        print('value is', values)
        if values['invest_cash_main'] + values['invest_inv_main'] != 4: # Might need to change that
            return 'The sum has to be 4 Rand'

    def before_next_page(self): # Here i will calculate whether the person was lucky or unlucky
        if (self.participant.id_in_session % 2) == 0: #If the participant has an even ID, which is the case in 50%
            self.participant.vars['payoff_luck'] = self.player.invest_cash_main # Unlucky
        else:
            self.participant.vars['payoff_luck'] = self.player.invest_cash_main + 3*self.player.invest_inv_main

# TREATMENT 2
#############

class Treatment_2_ctrl(Page):

    form_model = "player"
    form_fields = ['treat_2_ctrl']

    def is_displayed(self):
        return self.round_number == 1 and (self.participant.vars['treatment'] == 'one' or self.participant.vars['treatment'] == 'four')
        # and XXX (see otree template)

class Treatment_2_wc(Page):

    form_model = "player"
    form_fields = ['treat_2_wc']

    def is_displayed(self):
        return self.round_number == 1 and (self.participant.vars['treatment'] == 'two' or self.participant.vars['treatment'] == 'five')

class Treatment_2_rel(Page):

    form_model = "player"
    form_fields = ['treat_2_rel']

    def is_displayed(self):
        return self.round_number == 1 and self.participant.vars['treatment'] == 'three'

# EFFORT
########

class Effort_Intro(Page):

    def is_displayed(self):
        return self.round_number == 1

    # define timer. Has to be moved to the page before the effort task
    def before_next_page(self):
        import time
        self.participant.vars['expiry'] = time.time() + 45
        self.participant.vars['performance_main'] = 0

class Effort(Page):

    form_model = "player"
    form_fields = ['nb_inserted']

    # This conflicts with the other condition, so far displayed if ANY fits
    def is_displayed(self): # Not in last round(s) (display other pages there)
        return self.round_number < Constants.num_rounds

    timer_text = 'time left to complete this task'

    def get_timeout_seconds(self): # Update time left
        import time
        return self.participant.vars['expiry'] - time.time()

    def is_displayed(self): # If not, all remaining pages are displayed at once
        return self.get_timeout_seconds() > 3 # Combine with and?

    # This gives the total payoff (to be displayed, if necessary)
    def before_next_page(self):
        if self.player.nb_inserted == self.player.nb_correct:
            self.participant.vars['performance_main'] += Constants.payment_per_seq


# TREATMENT 3
#############

class Treatment_3_ctrl(Page):

    form_model = "player"
    form_fields = ['treat_3_ctrl']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and (self.participant.vars['treatment'] == 'one' or self.participant.vars['treatment'] == 'four')
        # and XXX (see otree template)

class Treatment_3_wc(Page):

    form_model = "player"
    form_fields = ['treat_3_wc']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and (self.participant.vars['treatment'] == 'two' or self.participant.vars['treatment'] == 'five')

class Treatment_3_rel(Page):

    form_model = "player"
    form_fields = ['treat_3_rel']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.participant.vars['treatment'] == 'three'

class Panas(Page): # This should be Treat3 and Panas

    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9','q10']

    # Maybe split this into 2-3 pages and add to previous module?

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    # Bonus payment. I already have the luck part, i will cap the effort part here
    def before_next_page(self):
        self.participant.vars['payoff_effort'] = self.participant.vars['performance_main']



class Panas_cntd(Page): # This should be Treat3 and Panas

    form_model = 'player'
    form_fields = ['q11', 'q12', 'q13', 'q14', 'q15','q16', 'q17', 'q18', 'q19', 'q20']

    # Maybe split this into 2-3 pages and add to previous module?

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    # Populate the payoff variable:
    def vars_for_template(self):
        if self.participant.vars['random_one'] == 1:
            self.participant.payoff = self.participant.vars['payoff_effort']
        elif self.participant.vars['random_one'] == 0:
            self.participant.payoff = self.participant.vars['payoff_luck']
    # Optional ,just to check
    def before_next_page(self):
        self.player.payoff_luck = self.participant.vars['payoff_luck']
        self.player.payoff_effort = self.participant.vars['payoff_effort']




page_sequence = [Treatment_main_ctrl_intro, Treatment_main_ctrl, Treatment_main_wc_intro, Treatment_main_wc, Treatment_main_rel_intro,
                 Treatment_main_rel,
                 Redistribution_1, Redistribution_2, Redistribution_3, Redistribution_4, Redistribution_4_red,
                 Investment, Treatment_2_ctrl, Treatment_2_wc, Treatment_2_rel, Effort_Intro, Effort, Treatment_3_ctrl,
                 Treatment_3_wc, Treatment_3_rel, Panas, Panas_cntd]

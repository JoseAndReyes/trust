from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'test_app'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3
    ENDOWMENT = cu(10)
    MULTIPLIER = 3
    INSTRUCTIONS_TEMPLATE = "test_app/instructions.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        doc="""Amount sent by P1""",
        label="Please enter an amount from 0 to {}:".format(C.ENDOWMENT),
    )
    sent_back_amount = models.CurrencyField(doc="""Amount sent back by P2""",
                                            label="Please enter an amount from 0 to {}:".format(
                                                C.ENDOWMENT*C.MULTIPLIER),
                                            min=cu(0),
                                            max=C.ENDOWMENT*C.MULTIPLIER)

class Player(BasePlayer):
    pass


# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1


class Send(Page):
    ''' Esta página solo es visible
    para el primer jugador, y permite el
    envío de dinero'''

    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        tripled_amount = group.sent_amount * C.MULTIPLIER
        return dict(tripled_amount=tripled_amount)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


class EsperarATodos(WaitPage):
    wait_for_all_groups = True
    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        subsession.group_randomly()

# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount

def sent_amount_choices(group: Group):
    return currency_range(0, C.ENDOWMENT, 1)

def sent_back_amount_choices(group: Group):
    return currency_range(0, group.sent_amount*C.MULTIPLIER, 1)

def creating_session(subsession):
    subsession.group_randomly()

page_sequence = [Introduction, Send, SendBackWaitPage, SendBack, ResultsWaitPage, Results, EsperarATodos]

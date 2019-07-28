from utils.helpers.helper_classes.house import House
from utils import global_data

class Player(House):
    def __init__(self, balance, deck):
        self.__balance = balance
        self.deck_object = deck
        self.__score = 0
        self.previous_cards = []

    def select_bet(self):
        while True:
            bet_amount = int(input(global_data.BET_AMOUNT_MSG))
            if bet_amount > self.get_balance():
                print(global_data.BALANCE_WARN_MSG)
                continue
            else:
                break
        return bet_amount

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance += amount
        return self.__balance

    def is_blackjack(self):
        return self.get_score() == global_data.PLAYER_STAND_CONSTANT
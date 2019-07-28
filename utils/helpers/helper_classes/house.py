from random import choice, randint
from utils.global_data import card_suits, card_face, card_values
from utils import global_data

class House:
    def __init__(self, deck):
        self.deck_object = deck
        self.__score = 0
        self.previous_cards = []

    def show_card(self):
        card_shown = {}
        random_suit = choice(list(self.deck_object.cards))
        random_face = choice(list(self.deck_object.cards[random_suit]))

        card_shown['face'] = random_face
        card_shown['suit'] = random_suit
        card_shown['value'] = card_values[random_face]

        del self.deck_object.cards[random_suit][random_face]

        if len(self.deck_object.cards[random_suit]) == 0:
            del self.deck_object.cards[random_suit]

        self.__decide_ace(card_shown['face'])

        self.previous_cards.append(card_shown)
        print('{0} : {2} of {1}'.format(self.__class__.__name__, card_shown['suit'].capitalize(), card_shown['face'].capitalize()))
        self.game_data()
        return card_shown

    def set_score(self, card_value = 0):
        print(card_value)
        if card_value == 0:
            self.__score = 0
        self.__score += card_value
        return self.__score

    def get_score(self):
        return self.__score

    def __decide_ace(self, card_face):
        if self.__class__.__name__ == 'Player' :
            if card_face == 'ace':
                upgrade_ace = True if input('Do you want to higher ace ? y / Y').lower()[0].startswith('y') else False
                self.set_score(card_values['ace']['higher'] if upgrade_ace else card_values['ace']['lower'])
            else:
                self.set_score(card_values[card_face])
        
        else:
        # will be adding probabilistic calculation of ace score 
        # depending on the remaining cards in the deck
            if card_face == 'ace':
                self.set_score(card_values['ace']['higher'])
            else:
                self.set_score(card_values[card_face])

    def game_data(self):
        print(global_data.game_data.format(self.__class__.__name__, self.get_score()))
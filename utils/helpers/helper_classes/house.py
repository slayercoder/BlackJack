from random import choice, randint
from utils.global_data import card_suits, card_face, card_values

class House:
    def __init__(self, deck):
        self.deck_object = deck
        self.score = 0
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

        # self.deck_object.update_deck(card_suits[suit_index], card_face[face_index])
        self.set_score(card_values[random_face])
        self.previous_cards.append(card_shown)
        print('{0} : {2} of {1}, current score is {3}'.format(self.__class__.__name__, card_shown['suit'].capitalize(), card_shown['face'].capitalize(), self.get_score()))
        return card_shown

    def set_score(self, card_value):
        print(card_value)
        self.score += card_value
        return self.score

    def get_score(self):
        return self.score

        # check if the suit for that index has any cards left, 
        # after this randomly select from the remaining card of that suit 
        
        # face_suit_name = suit_name_object[card_face[randint(0, len(card_face) - 1)]]
        # suit_name_object[face_suit_name] -= 1
        # suit_name_object.pop(face_suit_name)
        # return 'Card with suit {0} face {1}'.format(card_suits[suit_index], face_suit_name)



# if __name__ == '__main__':
#     pass
        
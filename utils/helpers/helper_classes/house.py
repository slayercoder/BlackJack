from random import randint
from utils.global_data import card_suits, card_face, card_values
class House:
    def __init__(self, deck):
        self.deck_object = deck
        self.score = 0

    def show_card(self):
        card_shown = {}
        while True:
            suit_index = randint(0, len(card_suits) - 1)
            if self.deck_object.check_suit_availability(card_suits[suit_index]):
                while True:
                    face_index = randint(0, len(card_face) - 1)
                    if self.deck_object.check_face_availability(card_suits[suit_index], card_face[face_index]):
                       card_shown['face'] = card_face[face_index]
                       card_shown['suit'] = card_suits[suit_index]
                       break
                    else:
                        continue
                break
        self.deck_object.update_deck(card_suits[suit_index], card_face[face_index])
        print('{0} Card with suit {1} face {2}'.format(self.__class__.__name__, card_shown['suit'], card_shown['face']))
        self.score += card_values[card_shown['face']]
        return card_shown

        # check if the suit for that index has any cards left, 
        # after this randomly select from the remaining card of that suit 
        
        # face_suit_name = suit_name_object[card_face[randint(0, len(card_face) - 1)]]
        # suit_name_object[face_suit_name] -= 1
        # suit_name_object.pop(face_suit_name)
        # return 'Card with suit {0} face {1}'.format(card_suits[suit_index], face_suit_name)



# if __name__ == '__main__':
#     pass
        
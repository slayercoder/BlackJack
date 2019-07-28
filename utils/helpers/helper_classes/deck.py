from utils.global_data import card_suits, card_face

def init_single_deck():
    single_deck_object = {}
    for face in card_face:
        single_deck_object[face] = 1

    return single_deck_object

class Deck:
    def __init__(self):
        self.cards = {
            card_suits[0]: init_single_deck(),
            card_suits[1]: init_single_deck(),
            card_suits[2]: init_single_deck(),
            card_suits[3]: init_single_deck()
        }
        print('Deck initialized')

    def check_suit_availability(self, suit_name):
        return True if len(self.cards[suit_name]) else False

    def check_face_availability(self, suit_name, face_name):
        return True if self.cards[suit_name][face_name] else False

    def update_deck(self, suit_name, face_name):
        self.cards[suit_name][face_name] -= 1

    def calculate_total_cards(self):
        total_cards = 0
        for suit in self.cards:
            for card_face_value in self.cards[suit]:
                total_cards += self.cards[suit][card_face_value]
        self.card_total = total_cards
        return self.card_total


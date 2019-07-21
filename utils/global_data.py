default_balance = 5000

# suits name constants
card_suit_spades = 'spades'
card_suit_clubs = 'clubs'
card_suit_hearts = 'hearts'
card_suit_diamonds = 'diamonds'

card_suits = (card_suit_spades, card_suit_clubs, card_suit_hearts, card_suit_diamonds)

# cards face values
card_face = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')

card_values = {
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
    'ace': {
        'lower': 1,
        'higher': 11
    }
}

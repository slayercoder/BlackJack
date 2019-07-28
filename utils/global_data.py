#initial player balance constant
PLAYER_DEFAULT_BALANCE = 5000

#initial player card drawing constant
PLAYER_INITIAL_TRY = 2

# BlackJack winning price factor
BLACKJACK_FACTOR = 1.5

# Threshold score for player
PLAYER_STAND_CONSTANT = 21

# Stand number for House
HOUSE_STAND_CONSTANT = 17

# Game Welcome Message
WELCOME_MSG = 'Welcome to BlackJack Casino Game\n\n'

# Play again message
PLAY_AGAIN_MSG = 'Do you want to continue play? y/Y or n/N'

# House drawing cards
HOUSE_DRAWING = 'House is drawing cards...'

# Error message string
ERROR_MSG_INPUT = 'Please give correct input'

# Select bet message
BET_AMOUNT_MSG = 'Select the bet amount from the chips '

# Balance not sufficient warning message
BALANCE_WARN_MSG = 'Not sufficient balance for the selected chip, please select bet again!!'

# Game data formatted text
game_data = '{}: Current score is {}'

# Blackjack message
BLACKJACK_MSG = 'BLACKJACK!!, player won'

# Player Hit or Stand message
HIT_STAND_MSG = 'Do you want to hit or stand ? '

# Message when player hits 21 score
PLAYER_AT_21_MSG = 'Player has scored 21, now house will play'

# Message after player crosses 21
PLAYER_BEYOND_21_MSG = 'Player has scored 21, now house will play'

# Fromat string when player decides to stand
player_stand_msg = 'Player stand, house to play, player score is {}'


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

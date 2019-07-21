from utils.helpers.helper_functions.welcome_screen import welcome_screen
from utils.helpers.helper_classes import player, house, deck
from utils.global_data import default_balance

welcome_screen()

#initialize the deck
deck = deck.Deck()

# initialize the player
player = player.Player(default_balance, deck)

#prompt the player to select a bet from the available balance
bet_amount = player.select_bet()

# player deals here
has_player_deal = player.player_deal()

# #uncomment below code once the body is in loop 
# if not has_player_deal:
#     print('Player didn't choose to deal, quitting!')
#     break


#initialize the house
house = house.House(deck)

#show the house cards one will be shown other will be hidden and adjust the available cards after this step
house.show_card()

# player will show two cards at ones
player.show_card()
player.show_card()

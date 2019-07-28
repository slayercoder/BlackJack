from utils.helpers import helper_functions
from utils.helpers.helper_classes import player, house, deck
from utils import global_data

helper_functions.welcome_screen()
continue_play = True

while continue_play:

    #initialize the deck
    deck_obj = deck.Deck()

    # initialize the player
    player_obj = player.Player(global_data.PLAYER_DEFAULT_BALANCE, deck_obj)

    #initialize the house
    house_obj = house.House(deck_obj)

    # loop will continue till the player has sufficient balance
    while player_obj.get_balance() > 0:
        player_obj.set_score()
        house_obj.set_score()

        #prompt the player to select a bet from the available balance
        bet_amount = player_obj.select_bet()

        #show the house cards one will be shown other will be hidden and adjust the available cards after this step
        house_obj.show_card()
        print(deck_obj.cards)

        # player will show two cards at ones
        for chance in range(global_data.PLAYER_INITIAL_TRY):
            player_obj.show_card()

        # has player got blackjack
        if player_obj.is_blackjack():
            print(global_data.BLACKJACK_MSG)
            player_obj.set_balance(bet_amount * (1 + global_data.BLACKJACK_FACTOR))
            continue
        
        helper_functions.subsequent_player_chances(player_obj)
        
        # House chances after player has a stand
        while player_obj.get_score() <= global_data.PLAYER_STAND_CONSTANT:
            if house_obj.get_score() < global_data.HOUSE_STAND_CONSTANT:
                print(global_data.HOUSE_DRAWING)
                house_card = house_obj.show_card()
                continue

            if house_obj.get_score() >= global_data.HOUSE_STAND_CONSTANT and  house_obj.get_score() <= global_data.PLAYER_STAND_CONSTANT:
                if house_obj.get_score() > player_obj.get_score():
                    print('Player lost !!')
                    player_obj.set_balance(-bet_amount)
                    print('player balance is {}'.format(player_obj.get_balance()))
                    break

                if house_obj.get_score() == player_obj.get_score():
                    print('Deal tied !! Push !!')
                    break

                else:
                    print('player won !!')
                    player_obj.set_balance(bet_amount) 
                    print('player balance is {}'.format(player_obj.get_balance()))
                    break

            if house_obj.get_score() > global_data.PLAYER_STAND_CONSTANT:
                print('house lost and player is winner')
                player_obj.set_balance(bet_amount)
                print('player balance is {}'.format(player_obj.get_balance()))
                break
        else:
            break

    continue_play = helper_functions.continue_play()
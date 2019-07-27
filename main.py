from utils.helpers.helper_functions.welcome_screen import welcome_screen
from utils.helpers.helper_classes import player, house, deck
from utils.global_data import default_balance

welcome_screen()
continue_play = True

deck = deck.Deck()
while continue_play:
#initialize the deck
    # initialize the player
    player = player.Player(default_balance, deck)

    #initialize the house
    house = house.House(deck)
# from here start looping
    while player.balance > 0:
        player.set_score(0)
        house.set_score(0)
        #prompt the player to select a bet from the available balance
        bet_amount = player.select_bet()

        # player deals here
        # has_player_deal = player.player_deal()

        # #uncomment below code once the body is in loop 
        # if not has_player_deal:
        #     print('Player didn\'t choose to deal, quitting!')
        #     break




        #show the house cards one will be shown other will be hidden and adjust the available cards after this step
        house.show_card()
        print(deck.cards)
        # player will show two cards at ones
        player.show_card()
        # print(deck.cards)
        player.show_card()

        if player.is_blackjack():
            print('Player won !!, score is {}'.format(player.get_score()))
            player.balance += 1.5 * bet_amount
            print('Player balance is {}'.format(player.balance))
            continue
        
        print(deck.cards)
        
        while True:
            hit_stand = input('Do you want to hit or stand ? ')
            if hit_stand == 'hit':
                player.show_card()

                print('player hit')

                if player.get_score() < 21:
                    continue
                elif player.get_score() == 21:
                    print('Player has scored 21, now house will play')
                    break
                else:
                    print('Player has crossed 21 and has lost !!')
                    break
            else:
                print('Player stand, house to play, player score is {}'.format(player.get_score()))
                break

        while player.get_score() <= 21:
            if house.get_score() <= 16:
                print('House is drawing cards...')
                house_card = house.show_card()
                continue

            if house.get_score() > 16 and  house.get_score() <= 21:
                print('House stopped play and will stand')
                if house.get_score() > player.get_score():
                    print('Player lost !!')
                    player.balance -= bet_amount
                    print('player balance is {}'.format(player.balance))
                    break
                else:
                    print('player won !!')
                    player.balance += bet_amount
                    print('player balance is {}'.format(player.balance))
                    break

            if house.get_score() > 21:
                print('house lost and player is winner')
                player.balance += bet_amount
                print('player balance is {}'.format(player.balance))
                break
        else:
            break
        # deciding winner
        # if house.get_score() > 1
continue_play = input('Do you want to continue play? y/Y or n/N').lower()[0] == 'y'
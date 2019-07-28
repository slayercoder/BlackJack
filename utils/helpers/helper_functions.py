from utils import global_data
 
def welcome_screen():
    print(global_data.WELCOME_MSG)

def continue_play():
    is_continue = False
    continue_play_input = input(global_data.PLAY_AGAIN_MSG)

    while True:
        if continue_play_input.lower().startswith('y'):
            is_continue = True
            break
        elif continue_play_input.lower().startswith('n'):
            is_continue = False
            break
        else:
            print(global_data.ERROR_MSG_INPUT)
            continue
    return is_continue

def subsequent_player_chances(player_obj):
    while True:
        hit_stand = input(global_data.HIT_STAND_MSG)
        if hit_stand == 'hit':
            player_obj.show_card()

            if player_obj.get_score() < global_data.PLAYER_STAND_CONSTANT:
                continue
            elif player_obj.get_score() == global_data.PLAYER_STAND_CONSTANT:
                print(global_data.PLAYER_AT_21_MSG)
                break
            else:
                print(global_data.PLAYER_BEYOND_21_MSG)
                break
        else:
            print(global_data.player_stand_msg.format(player_obj.get_score()))
            break
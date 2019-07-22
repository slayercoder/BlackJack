from utils.helpers.helper_classes.house import House

class Player(House):
    def __init__(self, balance, deck):
        self.balance = balance
        self.deck_object = deck
        self.score = 0
        self.previous_cards = []

    def select_bet(self):
        while True:
            bet_amount = int(input('Select the bet amount from the chips '))
            if bet_amount > self.balance:
                print('Not sufficient balance for the selected chip, please select bet again!!')
                continue
            else:
                break
        return bet_amount
    
    def player_deal(self):
        deal_input = str(input('Do you want to deal ?. Press "y" or "n"'))

        while len(deal_input) != 1:
            deal_input = input('Please enter valid input! "y / Y" or "n / N"')
        else:
            is_deal = True if deal_input.lower().startswith('y') == 'y' else False

        return is_deal

            

        

            


    
from random import shuffle
from os import system

def deal(num_to_deal, deck):
    cards_to_deal = []
    for i in range(num_to_deal):
        cards_to_deal.append(deck.pop())
    return cards_to_deal

def compute_score(cards):
    curr_score = 0
    for card in cards:
        curr_card_val = card[0]
        if curr_card_val.isdigit():
            curr_card_val = int(curr_card_val)
        elif curr_card_val == 'T' or curr_card_val == 'J' or curr_card_val == 'Q' or curr_card_val == 'K':
            curr_card_val = 10
        else:
            # NEED TO FIX THE ACE CASE
            curr_card_val = 11
        curr_score += curr_card_val
    return curr_score

def main():

    GAMES = 5
    INITIAL_BANKROLL = 100

    # Create a standard 52 card deck
    deck = []
    suits = ['C', 'D', 'H', 'S']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for suit in suits:
        for value in values:
            deck.append(value + suit)

    bankroll = INITIAL_BANKROLL

    for i in range(GAMES):

        print()
        print()
        print()

        # Shuffle the deck
        shuffle(deck)

        # Print player's bankroll
        print("Bankroll:", bankroll)

        # Deal palyer's cards
        player_cards = deal(2, deck)
        print("Player Cards:", player_cards)

        # Compute current score for player
        player_score = compute_score(player_cards)
        print("Player's Score:", player_score)

        print()

        # Calculate probability of winning (Monte Carlo simulation)
        for i in range(100)

        print()

        valid_input = False
        while not valid_input:
            bet = input("How much would you like to bet? ")
            if bet.isdigit():
                bet = int(bet)
                if bet >= 0 and bet <= bankroll:
                    valid_input = True
        print(bet)

        # Deal dealer's cards
        dealers_cards = deal(2, deck)
        print("Dealer Cards:", dealers_cards)

        # Compute current score for the dealer
        dealer_score = compute_score(dealers_cards)
        print("Dealer's Score:", dealer_score)

        # Determine winner
        if player_score > dealer_score:
            print("Player wins!")
            bankroll += bet
        elif player_score > dealer_score:
            print("Dealer wins!")
            bankroll -= bet
        else:
            print("Tie!")

        # Put cards back in deck
        while len(player_cards) > 0:
            deck.append(player_cards.pop())

        while len(dealers_cards) > 0:
            deck.append(dealers_cards.pop())

    # Print final bankroll
    print("Final bankroll:", bankroll)

if __name__ == '__main__':
    main()

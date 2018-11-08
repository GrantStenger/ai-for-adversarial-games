from random import shuffle

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

    GAMES = 100

    # Create a standard 52 card deck
    deck = []
    suits = ['C', 'D', 'H', 'S']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    for suit in suits:
        for value in values:
            deck.append(value + suit)

    for i in range(GAMES):

        # Shuffle the deck
        shuffle(deck)

        # Deal palyer 1's cards
        player1_cards = deal(2, deck)
        # print(player1_cards)

        # Compute current score for player 1
        player1_curr_score = compute_score(player1_cards)

        # Print initial score
        print(player1_curr_score)
        if player1_curr_score == 22:
            print("FUCK YEAH")

        # Put cards back in deck
        while len(player1_cards) > 0:
            deck.append(player1_cards.pop())

if __name__ == '__main__':
    main()

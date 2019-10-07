# Import Dependencies
from game import Game
from card import Card
import random

def main():

    # Parameters
    NUM_PLAYERS = 6
    ITERATIONS = 1

    # Constants
    suit_num_to_letter = {0: 'C', 1: 'D', 2: 'H', 3: 'S'}
    suit_letter_to_num = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
    value_num_to_letter = {
        1: 'A',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'T',
        11: 'J',
        12: 'Q',
        13: 'K'
    }
    value_letter_to_num = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13
    }

    # Initialize the game
    game = Game(NUM_PLAYERS)

    # Prompt user for input and check if valid
    is_valid = False
    while not is_valid:
        p1_hand = input("Input hand (e.g. A5, 27s, TQ): ")
        if (len(p1_hand) == 2 and p1_hand[0] in value_letter_to_num and \
                p1_hand[1] in value_letter_to_num):
            is_valid = True
            suited = False
        elif (len(p1_hand) == 3 and p1_hand[0] in value_letter_to_num and \
                p1_hand[1] in value_letter_to_num and p1_hand[2] == 's' and \
                p1_hand[0] != p1_hand[1]):
            is_valid = True
            suited = True
        else:
            print('input invalid')

    random_suits = random.sample(set(['S', 'H', 'C', 'D']), 2)

    if suited:
        p1_cards = [Card(p1_hand[0], random_suits[0]), Card(p1_hand[1], random_suits[0])]
    else:
        p1_cards = [Card(p1_hand[0], random_suits[0]), Card(p1_hand[1], random_suits[1])]

    # Remove these cards from the deck
    game.deck.remove(p1_cards)

    # For hundreds or thousands of games, count how often this hand wins
    wins = 0
    losses = 0
    ties = 0

    for i in range(ITERATIONS):

        # Deal player 2 their hole cards
        p2_cards = game.deck.deal(2)

        # Deal the river
        river = game.deck.deal(5)

        # Decide who won
        print(p1_cards)
        print(p2_cards)
        print(river)

        # Replace the cards that were dealt to player 2 and as the river
        game.deck.add(p2_cards)
        game.deck.add(river)
        game.deck.shuffle()


if __name__ == "__main__":
    main()

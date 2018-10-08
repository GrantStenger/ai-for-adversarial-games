""" Notes
Cards will be repreented in binary for fast runtime.
Details are explained in the README
"""

from random import shuffle, randrange, sample
# import random

# Constants
GAMES = 1
suit_num_to_letter = {0: 'C', 1: 'D', 2: 'H', 3: 'S'}
value_num_to_letter = {1: 'A',
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
                    13: 'K'}
suit_letter_to_num = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
value_letter_to_num = {'A': 1,
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
                       'K': 13}

def simulate_hand(player1):
    ## Outline

    # Start with two players
    # Player one gets pocket aces
    # Player two gets pocket tens
    # The river is drawn randomly
    # The winner is computed
    # The winner's win_count is incremented
    # The process is repeated until statistical significance is achieved

    # Create Deck
    deck = []
    for suit in range(4):
        bit_suit = '{0:02b}'.format(suit)
        for value in range(13):
            bit_value = '{0:04b}'.format(value+1)
            bit_card = bit_value + bit_suit
            deck.append(bit_card)
    # print(deck)
    shuffle(deck)
    # print(deck)
    deck.remove(player1[0])
    deck.remove(player1[1])
    # print(deck)

    player2 = []
    player2.append(deck.pop())
    player2.append(deck.pop())

    river = []
    for i in range(5):
        river.append(deck.pop())

    print("Player 1:")
    print_hand(player1)

    print("Player 2:")
    print_hand(player2)

    print("River: ")
    print_hand(river)

    decide_winner([player1, player2], river)

# Takes array of players and the river and decides which player won
# A value is calculated for each hand and these values are compared
def decide_winner(players, river):

    hand_values = []

    # 8: Straight Flush
    # Check all players for straights and flushes
    # Sort their hands by rank
    players_sorted_hands = []
    for player in players:
        players_sorted_hands.append(sorted(player + river))

    # Check for straight
    for hand in players_sorted_hands:
        longest_straight = 1
        current_straight = 1
        for i in range(1, len(hand)):
            print()
            print(hand[i])
            # Checks if new card is one more than the last card,
            # or current is an ace and last was a king
            if (int(hand[i-1], base=2) // 4) + 1 == (int(hand[i], base=2) // 4) or \
               ((int(hand[i-1], base=2) // 4) == '1101' and (int(hand[i], base=2) // 4 == '0001')):
                current_straight += 1
                print("current straight =", current_straight)
                print((int(hand[i-1], base=2) // 4) + 1, (int(hand[i], base=2) // 4))
                if current_straight > longest_straight:
                    longest_straight = current_straight
            elif int(hand[i-1], base=2) // 4 == int(hand[i], base=2) // 4:
                if (int(hand[i-2], base=2) // 4) + 1 == (int(hand[i], base=2) // 4) or \
                   ((int(hand[i-2], base=2) // 4) == '1101' and (int(hand[i], base=2) // 4 == '0001')):
                    current_straight += 1
                    print("current straight =", current_straight)
                    print((int(hand[i-2], base=2) // 4) + 1, (int(hand[i], base=2) // 4))
                    if current_straight > longest_straight:
                        longest_straight = current_straight
            elif int(hand[i-2], base=2) // 4 == int(hand[i], base=2) // 4:
                if (int(hand[i-3], base=2) // 4) + 1 == (int(hand[i], base=2) // 4) or \
                   ((int(hand[i-3], base=2) // 4) == '1101' and (int(hand[i], base=2) // 4 == '0001')):
                    current_straight += 1
                    print("current straight =", current_straight)
                    print((int(hand[i-3], base=2) // 4) + 1, (int(hand[i], base=2) // 4))
                    if current_straight > longest_straight:
                        longest_straight = current_straight
            elif int(hand[i-3], base=2) // 4 == int(hand[i], base=2) // 4:
                if (int(hand[i-4], base=2) // 4) + 1 == (int(hand[i], base=2) // 4) or \
                   ((int(hand[i-4], base=2) // 4) == '1101' and (int(hand[i], base=2) // 4 == '0001')):
                    current_straight += 1
                    print("current straight =", current_straight)
                    print((int(hand[i-4], base=2) // 4) + 1, (int(hand[i], base=2) // 4))
                    if current_straight > longest_straight:
                        longest_straight = current_straight
            else:
                current_straight = 1

        if longest_straight >= 5:
            print("STRAIGHT!!!!")
        print(longest_straight)

    # 7: Four of a Kind
    # 6: Full House
    # 5: Flush
    # 4: Straight
    # 3: Three of a Kind
    # 2: Two Pair

    ## 1: Pair
    # Pairs can be any value 2-A, 13 possibilities, 4 bits
    # 2=>0, 3=>1, 4=>2, 5=>3, 6=>4, 7=>5, 8=>6, 9=>7, T=>8, J=>9, Q=>10, K=>11, A=>12

    ## 0: High Card
    # There are 3750 possible high card combinations (12 bits)
    # Possible high cards are 9 to Ace
    # 9=>0, T=>1, J=>2, Q=>3, K=>4, A=>5
    # Possible second highest cards are 8 to King
    # 8=>0, 9=>1, T=>2, J=>3, Q=>4, K=>5
    # Possible third highest cards are 7 to Queen
    # 7=>0, 8=>1, 9=>2, T=>3, J=>4, Q=>5
    # Possible fourth highest cards are 5 to Jack
    # 5=>0, 6=>1, 7=>2, 8=>3, 9=>4, T=>5, J=>6
    # Possible fifth highest cards are 4 to 9
    # 4=>0, 5=>1, 6=>2, 7=>3, 8=>4, 9=>5

    print()

def print_hand(cards):
    for card in cards:
        print_bin_as_string(card)

def print_bin_as_string(card):
    suit = suit_num_to_letter[int(card, base=2) % 4]
    value = value_num_to_letter[int(card, base=2) // 4]
    print(value, suit)

def choose_hand(input):
    value1 = value_letter_to_num[input[0]]
    value2 = value_letter_to_num[input[1]]

    # If suited
    if len(input) == 3:
        # Choose 1 suit
        card1_bit_suit = '{0:02b}'.format(randrange(4))
        card2_bit_suit = card1_bit_suit
        # Choose distinct values
        card1_bit_value = '{0:04b}'.format(value1)
        card2_bit_value = '{0:04b}'.format(value2)

    # Else, if not suited
    else:
        # Choose 2 suits
        suits = sample([0, 1, 2, 3], 2)
        card1_bit_suit = '{0:02b}'.format(suits[0])
        card2_bit_suit = '{0:02b}'.format(suits[1])
        # Choose values
        card1_bit_value = '{0:04b}'.format(value1)
        card2_bit_value = '{0:04b}'.format(value2)

    card1_bit = card1_bit_value + card1_bit_suit
    card2_bit = card2_bit_value + card2_bit_suit

    return [card1_bit, card2_bit]

def main():

    hand = input("What hand would you like to check: ")

    player1 = choose_hand(hand)

    for i in range(GAMES):
        simulate_hand(player1)

if __name__ == "__main__":
    main()


"""
    values = {"2":2,
              "3":3,
              "4":4,
              "5":5,
              "6":6,
              "7":7,
              "8":8,
              "9":9,
              "T":10,
              "J":11,
              "Q":12,
              "K":13,
              "A":14}
"""

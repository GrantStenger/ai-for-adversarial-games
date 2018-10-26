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

# Start with two players
# Player one gets pocket aces
# Player two gets pocket tens
# The river is drawn randomly
# The winner is computed
# The winner's win_count is incremented
# The process is repeated until statistical significance is achieved
def simulate_hand(player1):

	# Create Deck
	deck = []
	for suit in range(4):
		bit_suit = '{0:02b}'.format(suit)
		for value in range(13):
			bit_value = '{0:04b}'.format(value+1)
			bit_card = bit_value + bit_suit
			deck.append(bit_card)
	shuffle(deck)

	# Remove player 1's cards from the deck
	deck.remove(player1[0])
	deck.remove(player1[1])

	# Assign player 2 their cards
	player2 = []
	player2.append(deck.pop())
	player2.append(deck.pop())

	# Draw river
	river = []
	for i in range(5):
		river.append(deck.pop())

	# Output players hole cards and the river
	print("Player 1:")
	print_hand(player1)

	print("Player 2:")
	print_hand(player2)

	print("River: ")
	print_hand(river)

	# Decide who the winner is
	winner = decide_winner_new([player1, player2], river)
	print("The winner is player " + str(winner) + "!")

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
		straight_high_card = -1
		for i in range(1, len(hand)):
			# Checks if new card is one more than the last card,
			# or current is an ace and last was a king
			if (int(hand[i-1], base=2) // 4) + 1 == (int(hand[i], base=2) // 4) or \
			   ((int(hand[i-1], base=2) // 4) == '1101' and (int(hand[i], base=2) // 4 == '0001')):
			   # increment length of longest straight
				current_straight += 1
				# If this is the longest straight seen so far, note that
				if current_straight > longest_straight:
					longest_straight = current_straight
					if longest_straight >= 5:
						straight_high_card = (int(hand[i], base=2) // 4)
			# If this next card is the same value as the next card,
			# keep straight length and move on.
			elif (int(hand[i-1], base=2) // 4) == (int(hand[i], base=2) // 4):
				current_straight = current_straight
			else:
				current_straight = 1

		if longest_straight >= 5:
			print("STRAIGHT!!!!")
			print(straight_high_card)
			## UPDATE HAND VALUE
			hand_values.append(4)
		else:
			# Assign this hand value 0
			hand_values.append(0)


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

def decide_winner_new(players, river):

	all_players_cards = []
	all_players_suits = []
	all_players_has_straight = []
	all_players_has_flush = []
	all_players_has_straight_flush = []
	all_players_four_of_a_kinds = []
	all_players_three_of_a_kinds = []
	all_players_pairs = []


	for player in players:
		player_cards = sorted(player + river)
		all_players_cards.append(player_cards)

		player_suits = [0, 0, 0, 0] # [clubs, diamonds, hearts, spades]
		all_players_suits.append(player_suits)

		# When a player gets a straight, -1 will become the straight's high card
		player_has_straight = -1
		all_players_has_straight.append(player_has_straight)

		# When a player gets a flush, -1 will become the straight's high card
		player_has_flush = -1
		all_players_has_flush.append(player_has_flush)

		# When a player gets a straight flush, -1 will become the straight's high card
		player_has_straight_flush = -1
		all_players_has_straight_flush.append(player_has_straight_flush)

		player_four_of_a_kinds = []
		all_players_four_of_a_kinds.append(player_four_of_a_kinds)

		player_three_of_a_kinds = []
		all_players_three_of_a_kinds.append(player_three_of_a_kinds)

		player_pairs = []
		all_players_pairs.append(player_pairs)

	# For each player, count the number of cards per suit
	for player_number, player_cards in enumerate(all_players_cards):
		for card in player_cards:
			if int(card, base=2) % 4 == 0:
				all_players_suits[player_number][0] += 1
			elif int(card, base=2) % 4 == 1:
				all_players_suits[player_number][1] += 1
			elif int(card, base=2) % 4 == 2:
				all_players_suits[player_number][2] += 1
			else:
				all_players_suits[player_number][3] += 1
		print(all_players_suits)
		print()

	# Check which players have flushes
	for player_num, player_suits in enumerate(all_players_suits):
		for suit, num_per_suit in enumerate(player_suits):
			if num_per_suit >= 5:
				print("We have a flush!!")
				print("player_num, player_suits")
				print(player_num, player_suits)
				print("suit, num_per_suit")
				print(suit, num_per_suit)
				# We need to find the highest card of their flush suit
				backwards_counter = 6
				current_card = all_players_cards[player_num][backwards_counter]
				print("current_card", current_card, str(int(current_card, base=2) // 4))
				while int(current_card, base=2) % 4 != suit:
					backwards_counter -= 1
					current_card = all_players_cards[player_num][backwards_counter]
					print("current_card", current_card)
				# If there is an ace, this is the highest card (values is 1)
				for forward_counter in range(4):
					potential_ace = all_players_cards[player_num][forward_counter]
					if int(potential_ace, base=2) % 4 == suit and int(potential_ace, base=2) // 4 == 1:
						current_card = potential_ace
				# Store the value of the highest card of this suit
				print("Output: ", str(int(current_card, base=2) // 4))
				all_players_has_flush[player_num] = int(card, base=2) // 4

	# Check which player have straights. Simultaneously check if straight-flush
	for player_num, cards in enumerate(all_players_cards):
		longest_straight = 1
		current_straight = 1
		straight_high_card = -1
		has_straight_flush = False
		num_consecutive_suit = 1
		for i in range(1, len(cards)):
			# Checks if new card is exactly one more than the last card,
			# or current is an ace and last was a king
			if (int(cards[i-1], base=2) // 4) + 1 == (int(cards[i], base=2) // 4) or \
			   ((int(cards[i-1], base=2) // 4) == '1101' and (int(cards[i], base=2) // 4 == '0001')):
			   	# Increment length of current straight
				current_straight += 1
				# If this card is the same suit as the previous card
				if int(cards[i-1], base=2) % 4 == int(cards[i], base=2) % 4:
					# Increment consecutive suited cards counter
					num_consecutive_suit += 1
				else:
					num_consecutive_suit = 1
				# Update longest straight length if necessary
				if current_straight > longest_straight:
					longest_straight = current_straight
					if longest_straight >= 5:
						straight_high_card = (int(cards[i], base=2) // 4)
					# Check if straight flush
					if num_consecutive_suit >= 5:
						has_straight_flush = True
						straight_flush_high_card = (int(cards[i], base=2) // 4)

			# If this next card is the same value as the next card,
			# keep straight length and move on.
			elif (int(cards[i-1], base=2) // 4) == (int(cards[i], base=2) // 4):
				pass
			else:
				current_straight = 1
				num_consecutive_suit = 1

		if longest_straight >= 5:
			print("STRAIGHT!!!!")
			print(straight_high_card)
			all_players_has_straight[player_num] = straight_high_card
			if has_straight_flush:
				print("STRAIGHT FUCKING FLUSH!!")
				all_players_has_straight_flush[player_num] = straight_flush_high_card


	# Check which player has the highest straight flush, if none then continue.
	players_with_straight_flushes = []
	for player_num in range(len(players)):
		# Check if a player has a straight flush
		if all_players_has_straight_flush[player_num] != -1:
			players_with_straight_flushes.append((player_num, all_players_has_straight_flush[player_num]))

	# If someone has a straight flush
	if len(players_with_straight_flushes) > 0:
		# Return player with highest straight flush hand
		current_highest_straight_flush = players_with_straight_flushes[0][1]
		current_winner = players_with_straight_flushes[0][0]
		for straight_flush_tuple in players_with_straight_flushes:
			if straight_flush_tuple[1] > current_highest_straight_flush:
				current_highest_straight_flush = straight_flush_tuple[1]
				current_winner = straight_flush_tuple[0]
		return current_winner


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

	hand = input("What hand would you like to check (e.g. A5, 27s, TQ): ")

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

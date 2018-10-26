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
	winners = decide_winners([player1, player2], river)

	# Print the winners!
	winners_string = ""
	for winner in winners:
		winners_string += str(winner + 1) + ", and "
	winners_string = winners_string[:-6]
	print("The winner is player " + winners_string + "!")

# This is the game logic that decides who wins.
# I am currently working to clean it up and optimize it.
# Right now it's really gross––apologies.
# Returns a list of winners (often just one, but accounts for case where several tie)
def decide_winners(players, river):

	all_players_cards = []
	all_players_suits = []
	all_players_has_straight = []
	all_players_has_flush = []
	all_players_has_straight_flush = []
	all_players_full_house = []
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

		player_four_of_a_kinds = -1
		all_players_four_of_a_kinds.append(player_four_of_a_kinds)

		player_full_house = [] # [three of a kind, pair]
		all_players_full_house.append(player_full_house)

		player_three_of_a_kinds = []
		all_players_three_of_a_kinds.append(player_three_of_a_kinds)

		player_pairs = []
		all_players_pairs.append(player_pairs)

	# print()
	# print(all_players_cards)
	# print(all_players_suits)
	# print(all_players_has_straight)
	# print(all_players_has_flush)
	# print(all_players_has_straight_flush)
	# print(all_players_full_house)
	# print(all_players_four_of_a_kinds)
	# print(all_players_three_of_a_kinds)
	# print(all_players_pairs)

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
	# print()
	# print(all_players_suits)

	# Check which players have flushes
	for player_num, player_suits in enumerate(all_players_suits):
		for suit, num_per_suit in enumerate(player_suits):
			if num_per_suit >= 5:
				# print("We have a flush!!")
				# print("player_num, player_suits")
				# print(player_num, player_suits)
				# print("suit, num_per_suit")
				# print(suit, num_per_suit)
				# We need to find the highest card of their flush suit
				backwards_counter = 6
				current_card = all_players_cards[player_num][backwards_counter]
				# print("current_card", current_card, str(int(current_card, base=2) // 4))
				while int(current_card, base=2) % 4 != suit:
					backwards_counter -= 1
					current_card = all_players_cards[player_num][backwards_counter]
					# print("current_card", current_card)
				# If there is an ace, this is the highest card (values is 1)
				for forward_counter in range(4):
					potential_ace = all_players_cards[player_num][forward_counter]
					if int(potential_ace, base=2) % 4 == suit and int(potential_ace, base=2) // 4 == 1:
						current_card = potential_ace
				# Store the value of the highest card of this suit
				# print("Output: ", str(int(current_card, base=2) // 4))
				all_players_has_flush[player_num] = int(current_card, base=2) // 4
	# print()
	# print(all_players_has_flush)

	# Check which player have straights. Simultaneously check if straight-flush
	for player_num, cards in enumerate(all_players_cards):
		longest_straight = 1
		current_straight = 1
		straight_high_card = -1
		straight_flush_high_card = -1
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
			# print("STRAIGHT!!!!")
			# print(straight_high_card)
			all_players_has_straight[player_num] = straight_high_card
			if has_straight_flush:
				# print("STRAIGHT FUCKING FLUSH!!")
				all_players_has_straight_flush[player_num] = straight_flush_high_card


	# Check which player has the highest straight flush
	players_with_straight_flushes = []
	for player_num in range(len(players)):
		# Check if a player has a straight flush
		if all_players_has_straight_flush[player_num] != -1:
			players_with_straight_flushes.append((player_num, all_players_has_straight_flush[player_num]))

	# If someone has a straight flush...
	if len(players_with_straight_flushes) > 0:
		# Return player with highest straight flush hand
		current_highest_straight_flush = players_with_straight_flushes[0][1]
		current_winner = [players_with_straight_flushes[0][0]]
		for straight_flush_tuple in players_with_straight_flushes[1:]:
			if straight_flush_tuple[1] > current_highest_straight_flush:
				current_highest_straight_flush = straight_flush_tuple[1]
				current_winner = [straight_flush_tuple[0]]
			elif straight_flush_tuple[1] == current_highest_straight_flush:
				# If any number of players share the same highest card, we need
				# to implement this logic. The following is currently not correct.
				current_winner.append(straight_flush_tuple[0])
		print("STRAIGHT FLUSH!!")
		return current_winner

	"""
	Check which players have for four of a kinds, three of a kinds, full houses,
	two pairs, and pairs and count the times a number appears in the hand.
	"""
	for player_num, cards in enumerate(all_players_cards):
		cards_seen = {int(cards[0], base=2) // 4: 1}
		for i in range(1, len(cards)):
			if int(cards[i], base=2) // 4 in cards_seen:
				cards_seen[int(cards[i], base=2) // 4] = cards_seen[int(cards[i], base=2) // 4] + 1
			else:
				cards_seen[int(cards[i], base=2) // 4] = 1
		# print("player num", player_num)
		# print("cards_seen", cards_seen)

		for card_val in cards_seen:
			if 4 == cards_seen[card_val]:
				all_players_four_of_a_kinds[player_num] = card_val
			if 3 == cards_seen[card_val]:
				all_players_three_of_a_kinds[player_num].append(card_val)
			if 2 == cards_seen[card_val]:
				all_players_pairs[player_num].append(card_val)

		# Check for four of a kinds is handled above

		# Check all three of a kind situations (different from full house)
		# If this player has two three of a kinds...
		if len(all_players_three_of_a_kinds[player_num]) == 2:
			# Create a full house by pick the largest to be the three of a kind
			# and picking the second largest for the pair.
			if all_players_three_of_a_kinds[player_num][0] > all_players_three_of_a_kinds[player_num][1]:
				all_players_full_house[player_num].append(all_players_three_of_a_kinds[player_num][0])
				all_players_full_house[player_num].append(all_players_three_of_a_kinds[player_num][1])
			else:
				all_players_full_house[player_num].append(all_players_three_of_a_kinds[player_num][1])
				all_players_full_house[player_num].append(all_players_three_of_a_kinds[player_num][0])
		elif len(all_players_three_of_a_kinds[player_num]) == 1 and len(all_players_pairs[player_num]) > 0:
			# If player has a three of a kind and at least one pair
			# Create a full house from the three of a kind and the largest pair
			all_players_full_house[player_num].append(all_players_three_of_a_kinds[player_num][0])
			current_largest_pair = all_players_pairs[player_num][0]
			for pair in all_players_pairs[player_num]:
				if pair > current_largest_pair:
					current_largest_pair = pair
			all_players_full_house[player_num].append(current_largest_pair)

	# print(all_players_pairs)
	# print(all_players_three_of_a_kinds)
	# print(all_players_full_house)
	# print(all_players_four_of_a_kinds)

	# Check which player have the highest four of a kind
	players_with_four_of_a_kinds = []
	for player_num in range(len(players)):
		if all_players_four_of_a_kinds[player_num] != -1:
			players_with_four_of_a_kinds.append((player_num, all_players_four_of_a_kinds[player_num]))
	# Return the player with the highest four of a kind
	if len(players_with_four_of_a_kinds) > 0:
		current_highest_foak = players_with_four_of_a_kinds[0][1]
		current_winner = [players_with_four_of_a_kinds[0][0]]
		for foak_tuple in players_with_four_of_a_kinds[1:]:
			if foak_tuple[1] > current_highest_foak:
				current_highest_foak = foak_tuple[1]
				current_winner = [foak_tuple[0]]
			elif foak_tuple[1] == current_highest_foak:
				# If any number of players share the same highest card, we need
				# to implement this logic. The following is currently not correct.
				current_winner.append(foak_tuple[0])
		print("FOUR OF A KIND!!")
		return current_winner

	# Check which player have the highest full house
	players_with_full_house = []
	for player_num in range(len(players)):
		if len(all_players_full_house[player_num]) != 0:
			players_with_full_house.append((player_num, all_players_full_house[player_num]))
	# Return the player with the highest full house
	if len(players_with_full_house) > 0:
		current_highest_full_house = players_with_full_house[0][1]
		current_winner = [players_with_full_house[0][0]]
		for full_house_tuple in players_with_full_house[1:]:
			if full_house_tuple[1] > current_highest_full_house:
				current_highest_full_house = full_house_tuple[1]
				current_winner = [full_house_tuple[0]]
			elif full_house_tuple[1] == current_highest_full_house:
				# If any number of players share the same highest card, we need
				# to implement this logic. The following is currently not correct.
				current_winner.append(full_house_tuple[0])
		print("FULL HOUSE!!")
		# print(players_with_full_house)
		return current_winner
	# NEED TO ADD TIE CASE

	# Check which player has the best flush
	players_with_flushes = []
	for player_num in range(len(players)):
		if all_players_has_flush[player_num] != -1:
			players_with_flushes.append((player_num, all_players_has_flush[player_num]))
	# Return the player with the best flush
	if len(players_with_flushes) > 0:
		# print()
		# print("players_with_flushes")
		# print(players_with_flushes)
		current_best_flush = players_with_flushes[0][1]
		current_winner = [players_with_flushes[0][0]]
		for flush_tuple in players_with_flushes[1:]:
			if flush_tuple[1] > current_best_flush:
				current_best_flush = flush_tuple[1]
				current_winner = [flush_tuple[0]]
			elif flush_tuple[1] == current_best_flush:
				# If any number of players share the same highest card, we need
				# to implement this logic. The following is currently not correct.
				current_winner.append(flush_tuple[0])
		print("FLUSH!")
		return current_winner
	# NEED TO ADD TIE CASE

	# Check which player has the best straight
	players_with_straights = []
	for player_num in range(len(players)):
		if all_players_has_straight[player_num] != -1:
			players_with_straights.append((player_num, all_players_has_straight[player_num]))
	# Return the player with the best straight
	if len(players_with_straights) > 0:
		current_best_straight = players_with_straights[0][1]
		current_winner = [players_with_straights[0][0]]
		for stright_tuple in players_with_straights[1:]:
			if stright_tuple[1] > current_best_straight:
				current_best_straight = stright_tuple[1]
				current_winner = [stright_tuple[0]]
			elif stright_tuple[1] == current_best_straight:
				# If any number of players share the same highest card, we need
				# to implement this logic. The following is currently not correct.
				current_winner.append(stright_tuple[0])
		print("STRAIGHT!")
		return current_winner
	# NEED TO ADD TIE CASE

	# Check which player have the highest three of a kind
	players_with_three_of_a_kinds = []
	for player_num in range(len(players)):
		if len(all_players_three_of_a_kinds[player_num]) != 0:
			players_with_three_of_a_kinds.append((player_num, all_players_three_of_a_kinds[player_num]))
	# Return the player with the highest three of a kind
	if len(players_with_three_of_a_kinds) > 0:
		current_highest_toak = players_with_three_of_a_kinds[0][1]
		current_winner = [players_with_three_of_a_kinds[0][0]]
		for toak_tuple in players_with_three_of_a_kinds[1:]:
			if toak_tuple[1] > current_highest_toak:
				current_highest_toak = toak_tuple[1]
				current_winner = [toak_tuple[0]]
			elif toak_tuple[1] == current_highest_toak:
				# If any number of players share the same highest card, we need
				# to implement this logic. The following is currently not correct.
				current_winner.append(toak_tuple[0])
		print("Three of a kind!")
		return current_winner
	# NEED TO ADD TIE CASE

	# Check which player has the best two pair
	players_with_two_pair = []
	for player_num in range(len(players)):
		if len(all_players_pairs[player_num]) >= 2:
			# Choose the two highest pairs
			if all_players_pairs[player_num][0] > all_players_pairs[player_num][1]:
				current_highest_two_pairs = [all_players_pairs[player_num][0], all_players_pairs[player_num][1]]
			else:
				current_highest_two_pairs = [all_players_pairs[player_num][1], all_players_pairs[player_num][0]]
			for i in range(2, len(all_players_pairs[player_num])):
				if all_players_pairs[player_num][i] > current_highest_two_pairs[0]:
					current_highest_two_pairs[0] = all_players_pairs[player_num][i]
				elif all_players_pairs[player_num][i] > current_highest_two_pairs[1]:
					current_highest_two_pairs[1] = all_players_pairs[player_num][i]
			players_with_two_pair.append((player_num, current_highest_two_pairs))
	# Return the player with the highest two pair
	if len(players_with_two_pair) > 0:
		current_highest_tp = players_with_two_pair[0][1]
		current_winner = [players_with_two_pair[0][0]]
		for tp_tuple in players_with_two_pair[1:]:
			if tp_tuple[1] > current_highest_tp:
				current_highest_tp = tp_tuple[1]
				current_winner = [tp_tuple[0]]
			elif tp_tuple[1] == current_highest_tp:
				# If any number of players share the same highest card, we need
				# to implement this logic. The following is currently not correct.
				current_winner.append(tp_tuple[0])
		print("Two pair!")
		return current_winner
	# NEED TO ADD TIE CASE

	# Check which player has the best pair
	players_with_pair = []
	for player_num in range(len(players)):
		if len(all_players_pairs[player_num]) >= 1:
			# Choose the highest pair
			current_highest_pair = [all_players_pairs[player_num][0]]
			for i in range(1, len(all_players_pairs[player_num])):
				if all_players_pairs[player_num][i] > current_highest_pair:
					current_highest_pair = all_players_pairs[player_num][i]
			players_with_pair.append((player_num, current_highest_pair))
	# Return the player with the highest two pair
	if len(players_with_pair) > 0:
		current_highest_pair = players_with_pair[0][1]
		current_winner = [players_with_pair[0][0]]
		for pair_tuple in players_with_pair[1:]:
			print("current_highest_pair", current_highest_pair)
			if current_highest_pair[0] != 1 and pair_tuple[1] > current_highest_pair:
				current_highest_pair = pair_tuple[1]
				current_winner = [pair_tuple[0]]
			elif pair_tuple[1] == current_highest_pair:
				# If any number of players share the same highest card, we need
				# to implement this logic. The following is currently not correct.
				current_winner.append(pair_tuple[0])
		print("Pair!")
		# print("Current winner", current_winner)
		return current_winner
	# Add Ace case
	# NEED TO ADD TIE CASE

	# Choose player with best high card
	current_best_high_card = all_players_cards[0][-1]
	current_winner = [0]
	for player_num, cards in enumerate(all_players_cards[1:]):
		if cards[-1] > current_best_high_card:
			current_best_high_card = cards[-1]
			current_winner = [player_num]
		elif cards[-1] == current_best_high_card:
			# If any number of players share the same highest card, we need
			# to implement this logic. The following is currently not correct.
			current_winner.append(player_num)
	print("High card:", current_best_high_card)
	return current_winner
	# NEED TO ADD TIE CASE




# Takes array of players and the river and decides which player won
# A value is calculated for each hand and these values are compared
def decide_winner_by_hand_value(players, river):

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

	# Prompt user for input and check if valid
	is_input_valid = False
	while not is_input_valid:
		hand = input("What hand would you like to check (e.g. A5, 27s, TQ): ")
		if (len(hand) == 2 and hand[0] in value_letter_to_num and hand[1] in value_letter_to_num) or (len(hand) == 3 and hand[0] in value_letter_to_num and hand[1] in value_letter_to_num and hand[2] == 's' and hand[0] != hand[1]):
			is_input_valid = True

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

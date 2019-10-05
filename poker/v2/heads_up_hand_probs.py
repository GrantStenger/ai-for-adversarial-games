# Dependencies
from deck import Deck

def analyze(player, community_cards):

	if player.has_a_straight_flush():
		return "Straight Flush"

def main():

	# Initialize deck and shuffle
	deck = Deck()
	deck.shuffle()

	# Deal 2 hole cards to each player
	player1 = []
	player2 = []
	for i in range(4):
		if i % 2 == 0:
			player1.append(deck.pop())
		else:
			player2.append(deck.pop())
	print("Player 1:", player1)
	print("Player 2:", player2)

	# Deal the 5 community cards
	community_cards = []
	for i in range(5):
		community_cards.append(deck.pop())
	print("Community Cards:", community_cards)

	# Analyze hand
	analyze(player1, community_cards)
	analyze(player2, community_cards)

if __name__ == "__main__":
	main()

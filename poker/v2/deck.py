from card import Card
import numpy as np

class Deck():

	def __init__(self):
		# The deck is an ordered list of the standard 52 playing cards
		self.deck = []

		# Add each card to the deck
		suits = ['H','C','D','S']
		values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
		for suit in suits:
			for value in values:
				self.deck.append(Card(value, suit))

	def __str__(self):
		return "\n".join(str(card) for card in self.deck)

	def shuffle(self):
		return np.random.shuffle(self.deck)

	def pop(self):
		return self.deck.pop()

	def deal(self, num_cards):
		selected_cards = []
		for i in range(num_cards):
			selected_cards.append(self.pop())
		return selected_cards

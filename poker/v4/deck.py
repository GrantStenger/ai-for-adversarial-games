# Import Dependencies
from card import Card
import numpy as np

class Deck:

	def __init__(self):

		# Initialize the list of cards
		self.cards = []

		# Add each card to the deck
		suits = ['H','C','D','S']
		values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
		for suit in suits:
			for value in values:
				self.cards.append(Card(value, suit))

		# Shuffle the deck
		self.shuffle()

	def shuffle(self):
		return np.random.shuffle(self.cards)

	def deal(self, num_cards):
		selected_cards = []
		for i in range(num_cards):
			selected_cards.append(self.cards.pop())
		return selected_cards

	def remove(self, cards):
		for card in cards:
			self.cards.remove(card)

	def add(self, cards):
		for card in cards:
			self.cards.append(card)

	def __str__(self):
		return "\n".join(str(card) for card in self.cards)

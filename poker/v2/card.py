class Card:

	def __init__(self, value, suit):
		self.suit = suit
		self.value = value

	def __str__(self):
		# return (str(self.value) + " of " + str(self.suit) + "s")
		return (str(self.value) + str(self.suit))

	def __repr__(self):
		return (str(self.value) + str(self.suit))

	def get_suit(self):
		return self.suit

	def get_value(self):
		return self.value
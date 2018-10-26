"""
Add low value of ace for straights
Separate poker.py into several files
"""

import numpy as np
import os
from collections import Counter

""" Classes """
class Deck:
	def __init__(self):
		self.deck = []

	def isEmpty(self):
		return len(self.deck) == 0

	def push(self, card):
		self.deck.append(card)

	def deal(self):
		return self.deck.pop()

	def peek(self):
		return self.deck[len(self.deck)-1]

	def size(self):
		return len(self.deck)

	def Print(self):
		for i in range(self.size()):
			print(self.deck[i])

	def shuffle(self):
		np.random.shuffle(self.deck)

class Card:
	def __init__(self, number, suit):
		self.number = number
		self.suit = suit

	def __repr__(self):
		return (str(self.number) + " of " + str(self.suit) + "s")

	def __str__(self):
		return (str(self.number) + " of " + str(self.suit) + "s")

	def __lt__(self, other_card):
		numbers = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
		return numbers.index(self.number) < numbers.index(other_card.number)
	def __le__(self, other_card):
		numbers = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
		return numbers.index(self.number) <= numbers.index(other_card.number)

class PrivateHand:
	def __init__(self, name):
		self.cards = []
		self.name = name

	def push(self, card):
		self.cards.append(card)

	def Print(self):
		print(self.name + "'s Cards: ")
		for i in range(self.size()):
			print(self.cards[i])

	def size(self):
		return len(self.cards)

	def analyze(self):
		if self.cards[0].number == self.cards[1].number:
			print("(Pair!)")
		else:
			print("(Not a pair)")

		if self.cards[0].suit == self.cards[1].suit:
			print("(Same suit)")
		else:
			print("(Different suits)")

class CommunityCards:
	def __init__(self):
		self.cards = []
		self.stageCount = 0

	def push(self, card):
		self.cards.append(card)

	def Print(self):
		self.stageCount += 1
		if self.stageCount == 1:
			print("The flop: ")
		elif self.stageCount == 2:
			print("The turn: ")
		elif self.stageCount == 3:
			print("The river: ")
		else:
			print("Error: Game should be over")
		for i in range(self.size()):
			print(self.cards[i])
		print()

	def size(self):
		return len(self.cards)


""" Functions """
def sortCards(cards):
	newList = []
	if cards[0] < cards[1]:
		newList.append(cards[0])
		newList.append(cards[1])
	else:
		newList.append(cards[1])
		newList.append(cards[0])

	for i in range(2, len(cards)):
		j = 0
		while j < len(newList):
			if cards[i] <= newList[j]:
				newList.insert(j, cards[i])
				j = len(newList)
			else:
				j += 1

		if newList[len(newList)-1] < cards[i]:
			newList.append(cards[i])

	return newList

def analyze(hole, community):
	cards = sortCards(hole.cards + community.cards)
	totalClubs = 0
	totalDiamonds = 0
	totalHearts = 0
	totalSpades = 0
	hasFourOfAKind = False
	hasFullHouse = False
	hasThreeOfAKind = False
	hasTwoPair = False
	hasPair = False
	hasFlush = False
	hasStraight = False
	fourOfAKinds = 0
	threeOfAKinds = 0
	pairs = 0
	fourOfAKindValue = ""
	threeOfAKindValues = []
	threeOfAKindValue = ""
	fullHouseValue = [] #[ToaK, pair]
	pairValues = []
	twoPairValue = [] #[higher, lower]
	pairValue = ""
	highCard = cards[0]
	handRank = ""

	for card in cards:
		# Count the number of cards per suit
		if card.suit == "club":
			totalClubs += 1
		elif card.suit == "diamond":
			totalDiamonds += 1
		elif card.suit == "heart":
			totalHearts += 1
		else:
			totalSpades += 1

		# Find high card
		if highCard < card:
			highCard = card

	if totalClubs >= 5 or totalDiamonds >= 5 or totalHearts >= 5 or totalSpades >= 5:
		hasFlush = True

	# Check for straight
	longestStraightLength = 1
	currentStraightLength = 1
	numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
	for i in range(1, len(cards)):
		if numbers.index(cards[i-1].number) + 1 == numbers.index(cards[i].number):
			currentStraightLength += 1
			if currentStraightLength > longestStraightLength:
				longestStraightLength = currentStraightLength
		elif numbers.index(cards[i-1].number) == numbers.index(cards[i].number):
			currentStraightLength = currentStraightLength
		else:
			currentStraightLength = 1
	if longestStraightLength >= 5:
		hasStraight = True

	# Check for Four of a Kind, Three of a Kind, Full House, Two Pair, and Pair
	# Count the times a number appears in the hand
	cardsSeen = {cards[0].number : 1}
	for i in range(1, len(cards)):
		if cards[i].number in cardsSeen:
			cardsSeen[cards[i].number] = cardsSeen[cards[i].number] + 1
		else:
			cardsSeen[cards[i].number] = 1

	for cardNum in cardsSeen:
		if 4 == cardsSeen[cardNum]:
			fourOfAKindValue = cardNum
			fourOfAKinds += 1
			hasFourOfAKind = True
		if 3 == cardsSeen[cardNum]:
			threeOfAKindValues.append(cardNum)
			threeOfAKinds += 1
		if 2 == cardsSeen[cardNum]:
			pairValues.append(cardNum)
			pairs += 1

	# Check for four of a kinds is handled above

	# Check all three of a kind situations
	if threeOfAKinds == 2:
		fullHouseValue = [threeOfAKindValues[1], threeOfAKindValues[0]]
		hasFullHouse = True
	elif threeOfAKinds == 1:
		if pairs > 0:
			fullHouseValue = [threeOfAKindValues[0], pairValues[pairs-1]]
			hasFullHouse = True
		else:
			threeOfAKindValue = threeOfAKindValues[0]
			hasThreeOfAKind = True
	else:
		# Check all pair situations
		if pairs > 1:
			twoPairValue = [pairValues[pairs-1], pairValues[pairs-2]]
			hasTwoPair = True
		elif pairs == 1:
			pairValue = pairValues[pairs-1]
			hasPair = True

	# Print results
	print("Analyze " + str(hole.name))
	print("Sorted cards: " + str(cards))
	if hasFourOfAKind:
		handRank = "Four of a Kind of " + str(fourOfAKindValue) + "s"
	elif hasFullHouse:
		handRank = "Full House: " + str(fullHouseValue)
	elif hasFlush:
		handRank = "Flush: " + str(hasFlush) # Flush of Diamonds
	elif hasStraight:
		handRank = "Straight: " + str(hasStraight)
	elif hasThreeOfAKind:
		handRank = "Three of a Kind: " + str(threeOfAKindValue)
	elif hasTwoPair:
		handRank = "Two Pair: " + str(twoPairValue[0]) + "s and " + str(twoPairValue[1]) + "s"
	elif hasPair:
		handRank = "Pair of " + str(pairValue) + "s"
	else:
		handRank = "High Card: " + str(highCard)


	print(handRank)


def dealPlayer(number, deck):
	player = PrivateHand("Player " + str(number))
	player.push(deck.deal())
	player.push(deck.deal())
	player.Print()
	print()
	player.analyze()
	print()
	return player

def winner(p1handRank, p2handRank):
	print()


""" main """
clear = lambda: os.system('clear')
clear()

print("Welcome to Grant's Casino!")
wantToPlay = input("Would you like to play? [y/n] ")
if wantToPlay == "y":
	clear()
	print("Great! Let me shuffle.")

	# Create a shuffled Deck with all 52 cards
	deck = Deck()
	numbers = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
	suits = ['club','diamond','heart','spade']
	for j in range(len(suits)):
		for i in range(len(numbers)):
			deck.push(Card(numbers[i],suits[j]))
	deck.shuffle()

	print("Here are your cards...")
	print()

	# Deal Player 1
	player1 = dealPlayer(1, deck)
	print()

	# Deal Player 1
	player2 = dealPlayer(2, deck)

	fold = input("Would you like to call or fold? [c/f] ")
	if fold == "c":
		clear()
		player1.Print()
		print()
		player2.Print()
		print()

		# Deal the flop
		CommunityCards = CommunityCards()
		CommunityCards.push(deck.deal())
		CommunityCards.push(deck.deal())
		CommunityCards.push(deck.deal())
		CommunityCards.Print()
		analyze(player1, CommunityCards)
		print()
		analyze(player2, CommunityCards)

		fold = input("Would you like to call or fold? [c/f] ")
		if fold == "c":
			clear()
			player1.Print()
			print()
			player2.Print()
			print()

			# Deal the turn
			CommunityCards.push(deck.deal())
			CommunityCards.Print()
			analyze(player1, CommunityCards)
			print()
			analyze(player2, CommunityCards)

			fold = input("Would you like to call or fold? [c/f] ")
			if fold == "c":
				clear()
				player1.Print()
				print()
				player2.Print()
				print()

				# Deal the river
				CommunityCards.push(deck.deal())
				CommunityCards.Print()
				analyze(player1, CommunityCards)
				print()
				analyze(player2, CommunityCards)
elif wantToPlay != "n":
	print("Sorry, I don't understand what that means.")

print("Bye! ")

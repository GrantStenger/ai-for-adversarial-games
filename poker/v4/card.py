class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return True if (self.suit == other.suit) and (self.value == other.value) else False

    def __str__(self):
        return "(" + self.suit + ", " + str(self.value) + ")"

from game import Game
from deck import Deck

def main():

	NUM_PLAYERS = 2
	INITIAL_STACK_SIZES = 100
	BIG_BLIND = 0
	SMALL_BLIND = 0

	game = Game(NUM_PLAYERS, INITIAL_STACK_SIZES, BIG_BLIND, SMALL_BLIND)

	game.play()

if __name__ == "__main__":
    main()

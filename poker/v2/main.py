from game import Game
from deck import Deck

def main():

	NUM_PLAYERS = 4
	INITIAL_STACK_SIZES = 100
	BIG_BLIND = 2
	SMALL_BLIND = 1

	game = Game(NUM_PLAYERS, INITIAL_STACK_SIZES, BIG_BLIND, SMALL_BLIND)

	game.play()

if __name__ == "__main__":
    main()
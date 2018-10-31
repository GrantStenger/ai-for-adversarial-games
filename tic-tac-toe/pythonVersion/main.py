#!/Users/Home/anaconda/bin/python

from Game import Game
from players.HumanPlayer import HumanPlayer
from players.ComputerPlayerLevel0 import ComputerPlayerLevel0
from players.ComputerPlayerLevel1 import ComputerPlayerLevel1
from players.ComputerPlayerLevel2 import ComputerPlayerLevel2
from players.ComputerPlayerLevel3 import ComputerPlayerLevel3

def main():
	game = Game()
	player1 = HumanPlayer("X")
	player2 = ComputerPlayerLevel3("O")
	game.play(player1, player2)

if __name__ == "__main__":
	main()

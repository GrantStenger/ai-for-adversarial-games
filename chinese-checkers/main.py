from game import Game
from player import HumanPlayer, ComputerPlayer

if __name__ == "__main__":
    game = Game([HumanPlayer("Human"), ComputerPlayer("Computer")])
    game.play()

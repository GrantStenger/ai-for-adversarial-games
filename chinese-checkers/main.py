from game import Game
from player import HumanPlayer, BeginnerComputerPlayer

if __name__ == "__main__":
    game = Game([HumanPlayer("Human", 1),
                BeginnerComputerPlayer("Computer", 2)])
    game.play()

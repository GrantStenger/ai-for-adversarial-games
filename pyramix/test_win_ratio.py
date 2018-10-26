from Game import Game
from players.HumanPlayer import HumanPlayer
from players.RandomComputerPlayer import RandomComputerPlayer
from players.GreedyComputerPlayer import GreedyComputerPlayer
from players.HalfGreedyComputerPlayer import HalfGreedyComputerPlayer
from players.DistanceComputerPlayer import DistanceComputerPlayer


def main():
    """ Outputs how many times each player wins.
    """
    
    win_nums = [0] * 3
    for i in range(100):
        # Initializes Players
        players = [DistanceComputerPlayer(3), GreedyComputerPlayer(), RandomComputerPlayer()]
        
        # Define vprint as an empty function
        vprint = lambda *a, **k: None

        # Initializes a Game with a depth of 3 and 2 colors
        game = Game(players, depth=7, num_colors=4, vprint=vprint)
        
        # Begins the game
        winner = game.play()
        if winner != -1:
            win_nums[winner] += 1

    print(win_nums)

if __name__ == "__main__":
    main()

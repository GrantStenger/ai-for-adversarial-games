from Game import Game
from players.HumanPlayer import HumanPlayer
from players.RandomComputerPlayer import RandomComputerPlayer
from players.GreedyComputerPlayer import GreedyComputerPlayer
from players.HalfGreedyComputerPlayer import HalfGreedyComputerPlayer


def main():
    """ Outputs how many times each player wins.
    """
    
    win_nums = [0] * 3
    for i in range(100):
        # Initializes Players
        players = [GreedyComputerPlayer(), HalfGreedyComputerPlayer(), RandomComputerPlayer()]
        
        # Initializes a Game with a depth of 3 and 2 colors
        game = Game(players, depth=7, num_colors=4)
        
        # Begins the game
        win_nums[game.play()] += 1

    print(win_nums)

if __name__ == "__main__":
    main()

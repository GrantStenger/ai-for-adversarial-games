from Game import Game
from players.Human import Human
from players.Random import Random
from players.Greedy import Greedy
from players.HalfGreedy import HalfGreedy
from players.Distance import Distance
from players.OptColorGreedy import OptColorGreedy


def main():
    """ Outputs how many times each player wins.
    """
    
    win_nums = [0] * 3
    for i in range(1000):
        # Initializes Players
        players = [Distance(3), Random(), OptColorGreedy()]
        
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

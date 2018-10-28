import sys
sys.path.append("..")
import argparse
import matplotlib.pyplot as plt
import numpy as np

from Game import Game
from players.Random import Random
from players.Greedy import Greedy
from players.HalfGreedy import HalfGreedy
from players.OptColorGreedy import OptColorGreedy


def main(_):
    """ Runs several experiments and graphs results.
    """

    experiment(Random(), HalfGreedy())
    experiment(HalfGreedy(), Greedy())
    #experiment(Random(), Greedy())
    #experiment(Random(), OptColorGreedy())
    #experiment(Greedy(), OptColorGreedy())
    #experiment(Random(), Greedy(), OptColorGreedy())

def experiment(player1, player2, player3=None):
    """ Runs a Game with the given Players.
    """

    # Define vprint as an empty function
    vprint = lambda *a, **k: None

    if not player3:
        result = [0] * 3
        for i in range(FLAGS.num_games):
            # Initializes Players
            players = [player1, player2]

            # Initializes a Game with a depth of 9 and 3 colors
            game = Game(players, depth=9, num_colors=3, vprint=vprint)

            # Begins the game
            winner = game.play()

            # Increments result
            if winner != -1:
                result[winner] += 1
            else:
                result[2] += 1
    else:
        result = [0] * 4
        for i in range(FLAGS.num_games):
            # Initializes Players
            players = [player1, player2, player3]

            # Initializes a Game with a depth of 15 and 4 colors
            game = Game(players, depth=15, num_colors=4, vprint=vprint)

            # Begins the game
            winner = game.play()

            # Increments result
            if winner != -1:
                result[winner] += 1
            else:
                result[3] += 1

    print(result)
    result = [int(float(x) / FLAGS.num_games * 100) for x in result]
    print(result)

    if player3:
        graph_results(player1, player2, result, player3)
    else:
        graph_results(player1, player2, result)

def graph_results(player1, player2, result, player3=None):
    """ Saves wins as bar graph.
    """

    player1_name = str(player1)[9:].partition(".")[0]
    player2_name = str(player2)[9:].partition(".")[0]
    if player3:
        player3_name = str(player3)[9:].partition(".")[0]

    x_names = [player1_name, player2_name, "Ties"]    
    if player3:
        x_names.insert(2, player3_name)
    x_pos = np.arange(len(x_names))

    plt.bar(x_pos, result, align="center")
    plt.xlabel("Player")
    plt.xticks(x_pos, x_names)
    plt.ylabel("Result Proportion")
    plt.title("Player vs Result Proportion")

    fig_name = player1_name + player2_name
    if player3:
        fig_name += player3_name
    fig_name += ".png"

    plt.savefig(fig_name)
    plt.close()

if __name__ == "__main__":
    # Instantiates an arg parser
    parser = argparse.ArgumentParser()

    # Establishes default arguments
    parser.add_argument("--num_games", type=int, default=100, help="Number of games to play")

    # Parse known arguments
    FLAGS, unparsed = parser.parse_known_args()

    # Run the experiment
    main([sys.argv[0]] + unparsed)

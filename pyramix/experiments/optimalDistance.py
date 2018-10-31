import sys
sys.path.append("..")
import matplotlib.pyplot as plt
import numpy as np

from Game import Game
from players.Random import Random
from players.Greedy import Greedy
from players.OptColorGreedy import OptColorGreedy
from players.Distance import Distance


def main():
    """ Outputs how many times each player wins.
    """

    DIST = 11
    GAMES = 10000

    dists = np.array([i for i in range(DIST)])
    result_dist = []
    result_gree = []
    result_optgree = []
    result_tie = []

    for i in range(DIST):
        result = [0] * 4
        for j in range(GAMES):
            # Initializes Players
            players = [Distance(i), Greedy(), OptColorGreedy()]

            # Define vprint as an empty function
            vprint = lambda *a, **k: None

            # Initializes a Game
            game = Game(players, depth=15, num_colors=4, vprint=vprint)

            # Begins the game
            winner = game.play()

            # Increments winner or ties as appropriate
            if winner != -1:
                result[winner] += 1
            else:
                result[3] += 1

        print(str(i) + ": " + str(result))
        result_dist.append(result[0] / GAMES * 100)
        result_gree.append(result[1] / GAMES * 100)
        result_rand.append(result[2] / GAMES * 100)
        result_tie.append(result[3] / GAMES * 100)

    y_stack = np.row_stack((result_dist, result_gree, result_optgree, result_tie))

    fig, ax = plt.subplots()
    ax.plot(dists, y_stack[0, :], label="Distance Wins", color="g")
    ax.plot(dists, y_stack[1, :], label="Greedy Wins", color="r")
    ax.plot(dists, y_stack[2, :], label="OptColorGreedy Wins", color="y")
    ax.plot(dists, y_stack[3, :], label="Ties", color="b")

    plt.xticks(np.arange(min(dists), max(dists), step=2))
    plt.xlabel("Distance")
    plt.ylabel("Result Proportion")
    plt.title("Distance vs. Result Proportion")
    plt.legend()
    plt.savefig("optDistToBeatGreedyAndOptColorGreedy.png", bbox_inches = "tight")


if __name__ == "__main__":
    main()

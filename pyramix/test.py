import torch

from Game import Game
from DQN import DQN
from players.OptColorGreedy import OptColorGreedy

def main():
    DEPTH = 15 
    NUM_COLORS = 4

    players = [OptColorGreedy(), OptColorGreedy(), OptColorGreedy()]

    game = Game(players, depth=DEPTH, num_colors=NUM_COLORS, vprint=print)

    dqn = DQN(DEPTH, NUM_COLORS)

    matrix = game.export_matrix_for_cnn()
    input = dqn.game_matrix_to_tensor(matrix)

    print(dqn.forward(input))

if __name__ == "__main__":
    main()

# Import Dependencies
import random
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt


# Constants
NUM_PLAYERS = 100

def compute_winner(player1, player2):
    
    # Initialize players' scores
    player1_score = 0
    player2_score = 0

    # Iterate through each battlefield until a player has won
    for i in range(10):

        # Compute and update each player's score
        if player1[i] > player2[i]:
            # Player 1 wins and is awarded points
            player1_score += i+1
        elif player1[i] < player2[i]:
            # Player 2 wins and is awarded points
            player2_score += i+1
        else:
            # They tie, and neither is awarded points
            pass

        # Determine if a player has won
        if player1_score >= 20 or player2_score >= 20:
            return (player1_score, player2_score)

    return (player1_score, player2_score)

def generate_random_allocations():
    allocation = [0] * 10
    for i in range(100):
        rand_slot = random.randint(1,10)
        allocation[rand_slot - 1] += 1
    return allocation

def display_sorted_ranking(players):
    
    players.sort(key=lambda x: x[1], reverse=True)
    
    grid = []
    for player in players:
        print(player[0], player[1])
        grid.append(player[0])

    new_grid = []
    for i in range(10):
        new_grid_row = []
        for col_num in range(10):
            cur_sub_cell_sum = 0
            for row_num in range(i*NUM_PLAYERS//10, (i+1)*NUM_PLAYERS//10):
                cur_sub_cell_sum += grid[row_num][col_num]
            new_grid_row.append(cur_sub_cell_sum)
        new_grid.append(new_grid_row)

    print(new_grid)

    plt.imshow(grid, cmap='hot')
    plt.show()

def main():

    players = []

    for i in range(NUM_PLAYERS):
        players.append([generate_random_allocations(), 0])

    for i in range(len(players)):
        for j in range(i+1, len(players)):
            final_score = compute_winner(players[i][0], players[j][0])
            players[i][1] += final_score[0]
            players[j][1] += final_score[1]

    for player in players:
        player[1] = player[1] / (NUM_PLAYERS-1)

    display_sorted_ranking(players)
    
if __name__ == "__main__":
    main()



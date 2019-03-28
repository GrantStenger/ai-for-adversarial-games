# Import Dependencies
import random
import matplotlib.pyplot as plt


# Constants
NUM_PLAYERS = 10000

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

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j]
    
    # plt.imshow(grid, cmap='hot')
    # plt.show()

def main():

    players = []

    for i in range(NUM_PLAYERS):
        players.append([generate_random_allocations(), 0])


    num_games = 0

    for i in range(len(players)):
        for j in range(i+1, len(players)):
            final_score = compute_winner(players[i][0], players[j][0])
            num_games += 1
            players[i][1] += final_score[0]
            players[j][1] += final_score[1]

    for player in players:
        player[1] = player[1] / (NUM_PLAYERS-1)

    display_sorted_ranking(players)
    
    print(num_games)

if __name__ == "__main__":
    main()



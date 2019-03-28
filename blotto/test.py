# Import Dependencies
import random
import matplotlib.pyplot as plt
import time

# Constants
NUM_PLAYERS = 1000

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

def generate_random_allocation():
    allocation = [0] * 10
    for i in range(100):
        rand_slot = random.randint(1,10)
        allocation[rand_slot - 1] += 1
    return allocation

def sort_players(players):
    players.sort(key=lambda x: x[1], reverse=True)
    return players

def players_to_grid(players):
    grid = []
    for player in players:
        grid.append(player[0])
    return grid

def create_new_grid(grid):
    new_grid = []
    for i in range(10):
        new_grid_row = []
        for col_num in range(10):
            cur_sub_cell_sum = 0
            for row_num in range(i*len(grid)//10, (i+1)*len(grid)//10):
                cur_sub_cell_sum += grid[row_num][col_num]
            sub_cell_avg = cur_sub_cell_sum * 10 / NUM_PLAYERS
            new_grid_row.append(sub_cell_avg)
        new_grid.append(new_grid_row)
    return new_grid

def plot_heat_map(grid):
    plt.imshow(grid, cmap='hot')
    plt.show()

def display_sorted_ranking(players):
    
    grid = players_to_grid(players)
    new_grid = create_new_grid(grid)
    #print(new_grid)

    plot_heat_map(new_grid)

def test_a_strategy(strategy): 
    
    strategy_score_sum = 0
    
    adversaries = []
    for i in range(NUM_PLAYERS):
        adversaries.append(generate_random_allocation())

    for adversary in adversaries:
        final_score = compute_winner(strategy, adversary)
        strategy_score_sum += final_score[0]

    avg_score = strategy_score_sum / NUM_PLAYERS
    return avg_score

def mutate(allocation):

    new_allocation = [e for e in allocation]

    to_add = random.sample(list(range(10)), 5)
    to_sub = [e for e in list(range(10)) if e not in to_add]
    
    #print('to add', to_add)
    #print('to sub', to_sub)
    
    to_sub = [i for i in to_sub if new_allocation[i] != 0]
    to_add = random.sample(to_add, len(to_sub))

    #print('to add', to_add)
    #print('to sub', to_sub)

    for i in to_add:
        new_allocation[i] += 1
    for i in to_sub:
        new_allocation[i] -= 1
    
    #print('new allocation', new_allocation)

    return new_allocation

def MuTaTe(allocation):

    new_allocation = [i for i in allocation]
    to_add_to = random.sample(list(range(10)), 5)
    for index in to_add_to:
        new_allocation[index] += 1

    to_subtract = [new_allocation.index(e) for e in new_allocation if e > 0 and e not in to_add_to]
    to_subtract = random.sample(to_subtract, 5)
    for index in to_subtract:
        new_allocation[index] -= 1
          
    return new_allocation

def old_mutate(allocation):
    new_allocation = []
    sample = random.sample(list(range(10)), 5)
    for i in range(10):
        if i in sample:
            new_allocation.append(allocation[i] + 1)
        else:
            new_allocation.append(allocation[i] - 1)

    return new_allocation

def play_round_robin(players):

    for i in range(len(players)):
        for j in range(i+1, len(players)):
            final_score = compute_winner(players[i][0], players[j][0])
            players[i][1] += final_score[0]
            players[j][1] += final_score[1]

    for player in players:
        player[1] = player[1] / (len(players)-1)

    return players

# Select the top 50% of models and additionally create a new set of mutated models
def create_new_player_set(players):
    
    new_players = []
    for player in players[:len(players)//2]:
        new_players.append(player[0])
        new_players.append(mutate(player[0]))

    players = []
    for player in new_players:
        players.append([player, 0])

    players = play_round_robin(players)
    players = sort_players(players)

    return players

def main():

    # Initialize an array of players
    players = []

    # Add random players to the array with starting score of 0
    for i in range(NUM_PLAYERS):
        players.append([generate_random_allocation(), 0])

    # Have all the players play each other in a round-robin tournament 
    players = play_round_robin(players)

    # Sort players by average score
    players = sort_players(players)


    winners = []
    winners.append(players[0][0])


    #print(players[0][0], 1)

    # Print out this first list of players
    #for player in players:
    #    print(player[0], player[1])
    
    # Display the ranked strategies in a heat map
    #display_sorted_ranking(players)


    # LET THEM PLAY AND LEARN
    # Delete the bottom 50% of competitors from the previous tournament and add a mutated 
    # copy of each of the winning 50% of competitors to the next round. 
    for i in range(1, 500):

        # In this funtion we take last round's competitors and create a new set
        players = create_new_player_set(players)
        
        if (i+1) % 10 == 0:
            print(players[0][0], i+1)
        winners.append(players[0][0])


        # Print out the players from best to worst
        #print()
        #for player in players:
        #    print(player[0], player[1])
        
        # Display these players' strategies as a heat map
        #if i % 20 == 0:
        #    display_sorted_ranking(players)
    
    # Finally display the heat map of the last round
    #display_sorted_ranking(players)

    #for player in players:
    #    print(player[0], player[1])
    #display_sorted_ranking(players)

    print()
    print()
    print()

    for winner in winners:
        print(winner)

    print()
    print()
    print()

    new_grid = create_new_grid(winners)
    #plot_heat_map(new_grid)
    #for item in new_grid:
    #    print(item)
    
    # Compute Final Ranking
    final_ranking = []
    for winner in winners:
        final_ranking.append([winner, 0])
    
    final_ranking = sort_players(play_round_robin(final_ranking))
    for player in final_ranking:
        print(player[0], player[1])



if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

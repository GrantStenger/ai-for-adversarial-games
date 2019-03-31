# Import Dependencies
import random
import matplotlib.pyplot as plt
import time

# Constants
NUM_PLAYERS = 1000
ITERATIONS = 500

def compute_winner(player1, player2):
    """
    Takes two allocations as input
    Returns the final score of their battle
    """

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
    """
    This generates and returns a random allocation of soldiers
    """
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

    to_sub = [i for i in to_sub if new_allocation[i] != 0]
    to_add = random.sample(to_add, len(to_sub))

    for i in to_add:
        new_allocation[i] += 1
    for i in to_sub:
        new_allocation[i] -= 1

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

def create_new_player_set(players):
    """
    Selects the top 50% of models and creates a new set of mutated models
    """

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

def generate_first_round_of_players():

    # Initialize an array of players
    players = []

    # Add random players to the array with starting score of 0
    for i in range(NUM_PLAYERS):
        players.append([generate_random_allocation(), 0])

    return players

def print_players(players):
    for player in players:
        print(player[0], player[1])

def main():

    # Generate the first round of players
    players = generate_first_round_of_players()

    # Have all the players play each other in a round-robin tournament
    players = play_round_robin(players)

    # Sort players by average score
    players = sort_players(players)

    # LET THEM PLAY AND LEARN
    # The following is a genetic algorithm that we will perform to create the
    # strongest players we can. We will delete the bottom 50% of competitors
    # from the previous tournament and add a mutated copy of each of the winning
    # 50% of competitors to the next round. These new players will compete and
    # this process will repeat. We will store the winner of each of these rounds
    # and will have them all compete in the final round.
    winners = []
    winners.append(players[0][0])

    for i in range(1, ITERATIONS):

        # In this funtion we take last round's competitors and create a new set
        players = create_new_player_set(players)

        # This helps to display our progress
        if (i+1) % 10 == 0:
            print(players[0][0], i+1)

        # Append the winner of this round to the final winners list
        winners.append(players[0][0])

    # Display winners list
    print()
    print()
    print()
    for winner in winners:
        print(winner)

    # Compute Final Ranking
    final_ranking = []
    for winner in winners:
        final_ranking.append([winner, 0])

    final_ranking = sort_players(play_round_robin(final_ranking))
    for player in final_ranking:
        print(player[0], player[1])

def final_test():

    processed_players = []
    for player in players_round5:
        processed_players.append([player, 0])

    players = sort_players(play_round_robin(processed_players))

    new_players = []
    for player in players[:len(players)//2]:
        new_players.append(player)

    for player in new_players:
        print(player)


if __name__ == "__main__":
    start_time = time.time()
    final_test()
    print("--- %s seconds ---" % (time.time() - start_time))

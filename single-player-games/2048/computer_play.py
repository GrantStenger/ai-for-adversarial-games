from GameState import GameState

# Define Constants
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
DEPTH_TO_SEARCH = 4

# Create game object (from GameState.py)
game_state = GameState(DEPTH_TO_SEARCH)

current_move_num = 0

# Run the game until game over
while not game_state.game_over:

    # Display the board
    if current_move_num % 10 == 0:
        game_state.display()

    # Prompt for user input
    choice = game_state.get_best_action()
    game_state.move(choice)

    # Check for game over sequence
    if game_state.game_over:
        game_state.display()
        game_state.update_high_score()
        print("Game Over.")
        print()

    current_move_num += 1

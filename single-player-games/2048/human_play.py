from GameState import GameState

# Define Constants
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3
DEPTH_TO_SEARCH = 3

# Create game object (from GameState.py)
game_state = GameState(DEPTH_TO_SEARCH)

# Run the game until game over
while not game_state.game_over:

    # Display the board
    game_state.display()

    # Prompt for user input
    choice = input("w, a, s, d, or q? ")

    # If user chooses left...
    if choice == "a":
        # Move left
        game_state.move(LEFT)

    # If user chooses right...
    elif choice == "d":
        # Move right
        game_state.move(RIGHT)

    # If user chooses up...
    elif choice == "w":
        # Move up
        game_state.move(UP)

    # If user chooses down...
    elif choice == "s":
        # Move down
        game_state.move(DOWN)

    # If user chooses to quit
    elif choice == "q":
        # Set gameOver to True
        game_state.game_over = True

    # Otherwise...
    else:
        print("That wasn't a choice")

    # Check for game over sequence
    if game_state.game_over:
        game_state.display()
        game_state.update_high_score()
        print("Game Over.")
        print()

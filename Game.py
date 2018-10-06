from random import shuffle
import string

from players.BasePlayer import BasePlayer
from Block import Block


class Game:
    """ Represents the game state.

        Keeps track of the players, board state, legal moves, and blocks remaining. Contains
        game-playing logic, and terminates game when appropriate.

        Attributes:
            players: A list of Players.
            depth: An integer representing the depth of the board.
            num_colors: An integer representing the number of block colors.

            current_player: An integer representing the index of the current Player in players.
            game_over: A boolean representing whether the game is over.
            blocks_left: An integer representing the amount of blocks left on the board.

            board: A nested list of Blocks representing the board.
            legal_moves: A list of legal moves given the board state.
    """

    def __init__(self, players, depth, num_colors):
        """ Initializes a Game.

            Args:
                players: A list of Players.
                depth: An integer representing the depth of the board.
                num_colors: An integer representing the number of block colors.
        """

        # Initialize argument values
        self.players = players
        self.depth = depth
        self.colors = self.generate_colors(num_colors)

        # Let players create a dict storing all 1 point tiles taken
        for player in players:
            player.set_colors(self.colors)

        # Initialize other default values
        self.current_player = 0
        self.game_over = False
        self.blocks_left = depth * (depth + 1) / 2

        # Initialize the board
        self.board = self.initialize_board(depth, num_colors)

        # Initalize the starting legal moves
        # MUST be called AFTER initialize_board
        self.legal_moves = self.initialize_legal_moves()

    def generate_colors(self, num_colors):
        """ Generates a list of block colors represented by ASCII letters.

            Args:
                num_colors: An integer representing the number of block colors. If num_colors
                    is greater than 26, raise an error.

            Returns:
                generated_colors: A list containing the generated colors.
                    For example, for num_colors = 2, it will return ["A", "B"].
        """

        # Raise an error if num_colors is greater than 26
        if num_colors > 26:
            raise ValueError("num_colors cannot be greater than 26.")

        # Initialize colors to ["A", "B", ..., "Z"]
        full_colors = list(string.ascii_uppercase)

        # Select the first num_colors items in colors
        generated_colors = full_colors[:num_colors]

        # Return the first num_colors colors
        return generated_colors

    def initialize_board(self, depth, num_colors):
        """ Initializes the board (represented as a nested list).

            Args:
                depth: An integer representing the depth of the board.
                num_colors: An integer representing the number of block colors.

            Returns:
                board: A nested list representing the initial board state.
        """

        # Calculates the total number of blocks on the board
        # How to extend to >2 dimensions?
        total_blocks = depth * (depth + 1) / 2

        # Calculates the number of blocks per color
        blocks_per_color = total_blocks / num_colors

        # If the colors can't be divided evenly, then raise an error
        if blocks_per_color != int(blocks_per_color):
            raise ValueError("Colors can't be divided evenly given this depth.")
        else:
            blocks_per_color = int(blocks_per_color)

        # Builds a shuffled list of Blocks
        blocks = []
        for i in range(num_colors):
            for j in range(blocks_per_color):
                # Instantiates a Block with the appropriate color and a value of 1
                new_block = Block(color=self.colors[i], value=1)
                # Adds the new Block to the list
                blocks.append(new_block)
        # Shuffles the list of Blocks
        shuffle(blocks)

        # Builds the initial board state
        # Must modify for >2 dimensions
        board = []
        # Adds positions on the x-axis
        for i in range(depth):
            row = []
            # Adds positions on the y-axis
            # As the x-axis increases, the maximum y decreases (via pyramid shape)
            for j in range(depth - i):
                # Add a random Block to the given position
                row.append(blocks.pop())
            # Add the completed x list to the board
            board.append(row)

        # Return the initialized board
        return board

    def make_move(self, position):
        """ Removes the Block in the given position and slides other
            blocks down accordingly.

            Args:
                position: An (x,y) tuple (must be extended for >2 dimensions).
        """
        # Remember to remove block from legal moves when detecting which position
        # loses a block.

        i = position[0]
        j = position[1]

        # Check if there is no block in both directions
        if (i == 0 or self.board[i - 1][j].color == "0") and \
           (j == 0 or self.board[i][j - 1].color == "0"):
            # Give block points and color to player
            self.players[self.current_player].score_block(self.board[i][j])

            # Remove block from board
            self.board[i][j].color = "0"
            self.board[i][j].value = 0

            # Remove block from legal moves
            self.legal_moves.remove((i, j))

        # Check if there is no block in the x direction
        elif i == 0 or self.board[i - 1][j].color == "0":
            # Give block points and color to player
            self.players[self.current_player].score_block(self.board[i][j])

            # Slide blocks down
            while not (j == 0 or self.board[i][j - 1].color == "0"):
                # Make new Block for new position
                # Don't just set equal because we want a copy, not a reference
                self.board[i][j] = Block(self.board[i][j - 1].color, self.board[i][j - 1].value)
                j -= 1

            # Remove final block from board
            self.board[i][j].color = "0"
            self.board[i][j].value = 0

            # Remove final block from legal moves
            self.legal_moves.remove((i, j))

        # Check if there is no block in the y direction
        elif j == 0 or self.board[i][j - 1].color == "0":
            # Give block points and color to player
            self.players[self.current_player].score_block(self.board[i][j])

            # Slide blocks down
            while not (i == 0 or self.board[i - 1][j].color == "0"):
                # Make new Block for new position
                # Don't just set equal because we want a copy, not a reference
                self.board[i][j] = Block(self.board[i - 1][j].color, self.board[i - 1][j].value)
                i -= 1

            # Remove final block from board
            self.board[i][j].color = "0"
            self.board[i][j].value = 0

            # Remove final block from legal moves
            self.legal_moves.remove((i, j))

        # Decrement blocks left
        self.blocks_left -= 1

    def score_bonus_blocks(self):
        """ Scores the bonus Blocks remaining in the base of the
            pyramid at the end of the game.

            (Add rules here later).
        """

        return 0

    def initialize_legal_moves(self):
        """ Initalizes the legal moves of the initial board state.

            Returns:
                legal_moves: A list of legal (x,y) moves.
        """

        legal_moves = []

        # Iterate over every board position (must be extended for >2 dimensions)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # If the move is on the edge of the board and there's not an empty cell above it
                # (i.e. it's locked on the bottom), or the move is in the center with an
                # empty cell above it, add it to the list of legal moves
                if (i == 0 and self.board[i][j - 1].color != "0") or \
                   (j == 0 and self.board[i - 1][j].color != "0") or \
                   self.board[i - 1][j].color == "0" or \
                   self.board[i][j - 1].color == "0":
                    legal_moves.append((i, j))

        # Return the list of legal (x,y) moves
        return legal_moves

    def update_legal_moves(self, move):
        """ Updates the legal moves of the current board state.

            Args:
                move: An (x,y) move.
        """

        # Set i and j to the initial x and y move positions
        i = move[0]
        j = move[1]

        # For every axis, iterate down until an empty Block is hit
        # Then, all adjacent positions become legal moves
        current_block = self.board[i][j]

        # Checks the x axis
        while current_block.color != "0" and j - 1 >= 0:
            j -= 1
            current_block = self.board[i][j]

        # Makes adjacent blocks legal
        if i > 0 and (i - 1, j) not in self.legal_moves and self.board[i - 1][j].color != "0":
            self.legal_moves.append((i - 1, j))
        if j > 0 and (i, j - 1) not in self.legal_moves and self.board[i][j - 1].color != "0":
            self.legal_moves.append((i, j - 1))

        # Resets i and j
        i = move[0]
        j = move[1]

        # Checks the y axis
        while current_block.color != "0" and i - 1 >= 0:
            print(str(i))
            i -= 1
            current_block = self.board[i][j]

        # Makes adjacent blocks legal
        if i > 0 and (i - 1, j) not in self.legal_moves and self.board[i - 1][j].color != "0":
            self.legal_moves.append((i - 1, j))
        if j > 0 and (i, j - 1) not in self.legal_moves and self.board[i][j - 1].color != "0":
            self.legal_moves.append((i, j - 1))

        self.legal_moves.sort()

    def pretty_print(self):
        """ Prints board, legal moves, player scores and colors
        """

        print()
        # Prints the board in a pretty manner
        # Spaces stores the number of spaces between each tile
        spaces = 4
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # Prints each tile (consisting of two characters)
                print(str(self.board[i][j]), end="")
                if (str(self.board[i][j]) == '0'):
                    print (" ", end="")

                # Prints space number of spaces each tile and vertical division between tiles
                for k in range(spaces):
                    print(" ", end="")
                    if k == (spaces + 2) // 2 - 2:
                        print("|", end="")
            print()
            # Prints a line of underscores between each row of tiles
            for j in range(len(self.board[i])):
                for k in range(spaces + 2):
                    print("_", end="")
                    if k == (spaces + 2) // 2:
                        print("|", end="")
                        if j == len(self.board[i]) - 1:
                            break
            print()
        print()

        # Prints players and scores
        for i, player in enumerate(self.players):
            print("Player " + str(i + 1) + ": ")
            player.pretty_print()
        print()

        # Prints legal moves
        print("Legal moves: " + str(self.legal_moves))
        print()

        # Prints current player
        print("Player " + str(self.current_player + 1) + "'s move.")

    def pretty_print_for_end(self):
        """ Prints board and score, and winner at the end of the game.
        """

        print()

        # Prints players and scores
        for i, player in enumerate(self.players):
            print("Player " + str(i + 1) + ": ")
            player.pretty_print()
        print()

        # Prints winner and score
        # Could be more pythonic, but we need the winner number which makes it less elegant
        winner = BasePlayer()
        winner_num = -1
        for i, player in enumerate(self.players):
            if player.score > winner.score:
                winner = player
                winner_num = i

        print("Winner: Player " + str(winner_num + 1) + " Score: " + str(winner.score))

    def play(self):
        """ Runs gameplay until the game is over, then scores bonus Blocks.
        """

        parameters = "Players: " + str(len(self.players))
        parameters += " Depth: " + str(self.depth)
        parameters += " Colors: " + str(len(self.colors))

        # Print game parameters
        print("------------PYRAMIX------------")
        print(parameters)

        # Runs gameplay until only the base Blocks remain
        while not self.game_over:
            # Prints the current game state
            self.pretty_print()

            # Current player evaluates legal moves and selects the optimal (x,y) position
            move = self.players[self.current_player].evaluate_moves(self.legal_moves)

            # Applies the move that the player chose
            self.make_move(move)

            # If only the base Blocks remain, terminate the game
            if self.blocks_left == self.depth:
                self.game_over = True
            if len(self.legal_moves) == 0:
                self.game_over = True

            # Updates legal moves given the player's move choices
            self.update_legal_moves(move)

            # Makes the next player the current player
            self.current_player = (self.current_player + 1) % len(self.players)

        # Scores bonus blocks
        self.score_bonus_blocks()

        # Prints the endgame and winner
        self.pretty_print_for_end()

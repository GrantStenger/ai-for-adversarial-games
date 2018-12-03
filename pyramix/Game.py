from random import shuffle
from random import randint
import numpy as np
import string

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

    def __init__(self, players, depth, num_colors, vprint):
        """ Initializes a Game.

            Args:
                players: A list of Players.
                depth: An integer representing the depth of the board.
                num_colors: An integer representing the number of block colors.
                vprint: A function which is equivalent to print if verbose, empty if not verbose.
        """

        # Initialize argument values
        self.players = players
        self.depth = depth
        self.colors = self.generate_colors(num_colors)
        self.vprint = vprint

        # Let players create a dict storing all 1 point tiles taken
        for player in players:
            player.set_colors(self.colors)

        # Initialize other default values
        self.current_player = 0
        self.game_over = False
        self.blocks_left = depth * (depth + 1) / 2

        # Initialize the board
        self.board = self.initialize_board(num_colors)

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

    def initialize_board(self, num_colors):
        """ Initializes the board (represented as a nested list).

            Args:
                num_colors: An integer representing the number of block colors.

            Returns:
                board: A nested list representing the initial board state.
        """

        # Calculates the total number of blocks on the board
        # How to extend to >2 dimensions?
        total_blocks = self.depth * (self.depth + 1) / 2

        # If the players will have unequal amounts of turns, raise an error
        turns_per_player = (total_blocks - self.depth) / len(self.players)
        if turns_per_player != int(turns_per_player):
            raise ValueError("Players will have unequal turns given this depth and num_players")

        # Calculates the number of blocks per color
        blocks_per_color = total_blocks / num_colors

        # If the colors can't be divided evenly, then raise an error
        if blocks_per_color != int(blocks_per_color):
            raise ValueError("Colors can't be divided evenly given this depth.")
        else:
            blocks_per_color = int(blocks_per_color)

        # Builds the points of the Blocks
        # Let 6/10 be 1 point, 3/10 be 2 points, 1/10 be 3 points
        one_point_blocks_per_color = round(0.6 * blocks_per_color)
        two_point_blocks_per_color = round(0.3 * blocks_per_color)
        three_point_blocks_per_color = round(0.1 * blocks_per_color)

        # Make sure the points add up
        if one_point_blocks_per_color + two_point_blocks_per_color + three_point_blocks_per_color != blocks_per_color:
            raise ValueError("Points can't be divided evenly given this depth and num_colors")

        # Build an array of points
        points = []
        points[:one_point_blocks_per_color] = [1] * one_point_blocks_per_color
        points[one_point_blocks_per_color + 1:two_point_blocks_per_color] = [2] * two_point_blocks_per_color
        points[one_point_blocks_per_color + two_point_blocks_per_color + 1:] = [3] * three_point_blocks_per_color

        # Builds a shuffled list of Blocks
        blocks = []
        for i in range(num_colors):
            for j in range(blocks_per_color):
                # Instantiates a Block with the appropriate color and points
                new_block = Block(color=self.colors[i], value=points[j])
                # Adds the new Block to the list
                blocks.append(new_block)
        # Shuffles the list of Blocks
        shuffle(blocks)

        # Builds the initial board state
        # Must modify for >2 dimensions
        board = []
        # Adds positions on the x-axis
        for i in range(self.depth):
            row = []
            # Adds positions on the y-axis
            # As the x-axis increases, the maximum y decreases (via pyramid shape)
            for j in range(self.depth - i):
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

            The player with the most 1-point blocks of that color get the points; if there is a
            tie, nobody gets the points.
        """

        self.vprint()
        self.vprint("Scoring bonus blocks...")

        for color in self.colors:
            # Creates a list of how many 1-point blocks of this color everyone has
            ones_of_color = [player.bonuses_taken_per_color[color] for player in self.players]

            # Finds max number
            max_ones_of_color = max(ones_of_color)

            # Ends if there is more than one max player
            if ones_of_color.count(max_ones_of_color) == 1:
                points_scored = 0

                # Finds the player with the most 1-point blocks of that color
                max_player = [player for player in self.players if player.bonuses_taken_per_color[color] == max_ones_of_color][0]
                player_index = self.players.index(max_player)

                # Change to be more efficient and not have to search the whole board
                for row in self.board:
                    for block in row:
                        if block.color == color:
                            max_player.score_block(block)
                            points_scored += block.value
                self.vprint()
                self.vprint("Player " + str(player_index + 1) + " won the color " + color + " and scored " + str(points_scored) + " points.")
            else:
                self.vprint()
                self.vprint("There was a tie for the color " + color + ".")

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
        if i > 0 and (i - 1, j) not in self.legal_moves and \
           self.board[i - 1][j].color != "0":
            self.legal_moves.append((i - 1, j))
        if j > 0 and (i, j - 1) not in self.legal_moves and \
           self.board[i][j - 1].color != "0":
            self.legal_moves.append((i, j - 1))
        if current_block.color == "0" and (i != self.depth - 2 and j != 0) and \
           (i + 1 + j) < self.depth and self.board[i + 1][j].color != "0" and \
           (i + 1, j) not in self.legal_moves:
            self.legal_moves.append((i + 1, j))
        if current_block.color == "0" and (i != 0 and j != self.depth - 2) and \
           (i + j + 1) < self.depth and self.board[i][j + 1].color != "0" and \
           (i, j + 1) not in self.legal_moves:
            self.legal_moves.append((i, j + 1))

        # Resets i and j
        i = move[0]
        j = move[1]

        # For every axis, iterate down until an empty Block is hit
        # Then, all adjacent positions become legal moves
        current_block = self.board[i][j]

        # Checks the y axis
        while current_block.color != "0" and i - 1 >= 0:
            i -= 1
            current_block = self.board[i][j]

        # Makes adjacent blocks legal
        if i > 0 and (i - 1, j) not in self.legal_moves and self.board[i - 1][j].color != "0":
            self.legal_moves.append((i - 1, j))
        if j > 0 and (i, j - 1) not in self.legal_moves and self.board[i][j - 1].color != "0":
            self.legal_moves.append((i, j - 1))
        if current_block.color == "0" and (i != self.depth - 2 and j != 0) and (i + 1 + j) < self.depth and self.board[i + 1][j].color != "0" and (i + 1, j) not in self.legal_moves:
            self.legal_moves.append((i + 1, j))
        if current_block.color == "0" and (i != 0 and j != self.depth - 2) and (i + j + 1) < self.depth and self.board[i][j + 1].color != "0" and (i, j + 1) not in self.legal_moves:
            self.legal_moves.append((i, j + 1))

        # Resets i and j
        i = move[0]
        j = move[1]

        # Removes block from legal moves if removing it would expose the board
        # Case when the block is taken from the bottom
        if (i + j + 1) == self.depth and (i, j) in self.legal_moves:
            if (i == 0 or (i > 0 and self.board[i - 1][j].color == "0")) and \
               (j == 0 or (j > 0 and self.board[i][j - 1].color == "0")):
                self.legal_moves.remove((i, j))
            if (i + 1, j - 1) in self.legal_moves:
                if j <= 1 or self.board[i + 1][j - 2].color == "0":
                    self.legal_moves.remove((i + 1, j - 1))
            if (i - 1, j + 1) in self.legal_moves:
                if i <= 1 or self.board[i - 2][j + 1].color == "0":
                    self.legal_moves.remove((i - 1, j + 1))
        # Case when the block is taken from the second to the bottom
        elif (i + j + 2) == self.depth and self.board[i][j].color == "0":
            if (i + 1, j) in self.legal_moves:
                if j == 0 or self.board[i + 1][j - 1].color == "0":
                    self.legal_moves.remove((i + 1, j))
            if (i, j + 1) in self.legal_moves:
                if i == 0 or self.board[i - 1][j + 1].color == "0":
                    self.legal_moves.remove((i, j + 1))

        self.legal_moves.sort()

    def pretty_print_board(self):
        """ Prints the board
        """

        # Prints the board in a pretty manner
        # Spaces stores the number of spaces between each tile
        spaces = 4
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # Prints each tile (consisting of two characters)
                self.vprint(str(self.board[i][j]), end="")
                if (str(self.board[i][j]) == '0'):
                    self.vprint(" ", end="")

                # Prints space number of spaces each tile and vertical division between tiles
                for k in range(spaces):
                    self.vprint(" ", end="")
                    if k == (spaces + 2) // 2 - 2:
                        self.vprint("|", end="")
            self.vprint()
            # Prints a line of underscores between each row of tiles
            for j in range(len(self.board[i])):
                for k in range(spaces + 2):
                    self.vprint("_", end="")
                    if k == (spaces + 2) // 2:
                        self.vprint("|", end="")
                        if j == len(self.board[i]) - 1:
                            break
            self.vprint()

    def pretty_print(self):
        """ Prints board, legal moves, player scores and colors
        """

        self.vprint()
        self.pretty_print_board()
        self.vprint()

        # Prints players and scores
        for i, player in enumerate(self.players):
            self.vprint("Player " + str(i + 1) + ": ")
            player.pretty_print(self.vprint)
        self.vprint()

        # Prints legal moves
        self.vprint("Legal moves: " + str(self.legal_moves))
        self.vprint()

        # Prints current player
        self.vprint("Player " + str(self.current_player + 1) + "'s move.")

    def pretty_print_for_end(self):
        """ Prints board and score, and winner at the end of the game.
        """

        self.vprint()

        # Prints players and scores
        for i, player in enumerate(self.players):
            self.vprint("Player " + str(i + 1) + ": ")
            player.pretty_print(self.vprint)
        self.vprint()

        # Prints winner and score
        winner = max(self.players, key=lambda player: player.score)
        winner_num = self.players.index(winner) + 1

        # Determine if there is a tie
        def has_max_score(player, score):
            return player.score == score
        num_players_with_max_score = sum(1 for player in self.players if has_max_score(player, winner.score))

        if num_players_with_max_score == 1:
            self.vprint("Winner: Player " + str(winner_num) + " Score: " + str(winner.score))
            return winner_num - 1
        else:
            self.vprint("There is a tie. Score: " + str(winner.score))
            return -1
    
    def export_matrix_for_cnn(self):
        matrix = np.zeros((3 * len(self.colors), self.depth, self.depth), dtype=np.int) 

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                block = self.board[i][j]
                if block.color != "0":
                    matrix[3 * self.colors.index(block.color) + block.value - 1][i][j] = 1

        return matrix

    def setup(self):
        parameters = "Players: " + str(len(self.players))
        parameters += " Depth: " + str(self.depth)
        parameters += " Colors: " + str(len(self.colors))

        # Print game parameters
        self.vprint()
        self.vprint("------------PYRAMIX------------")
        self.vprint(parameters)

        # Sets up random player order
        self.players_order = [i for i in range(len(self.players))]
        shuffle(self.players_order)
        self.current_player = self.players_order[0]

    def step(self, move):
        """ Steps one move of gameplay.

            Returns:
                state: The initial board matrix
                action: The move passed in as a parameter
                reward: The increase in score for the player
                next_state: The next board matrix
        """

        initial_score = self.players[self.current_player].score
        state = self.export_matrix_for_cnn()
        action = move
        
        self.make_move(move)

        # If only the base Blocks remain, terminate the game
        if self.blocks_left == self.depth:
            self.game_over = True
        if len(self.legal_moves) == 0:
            self.game_over = True

        if self.game_over:
            self.score_bonus_blocks()

        # Updates legal moves given the player's move choices
        self.update_legal_moves(move)

        reward = self.players[self.current_player].score - initial_score
        next_state = self.export_matrix_for_cnn()

        # Re-randomize player order if necessary, otherwise increment player
        current_player_index = self.players_order.index(self.current_player)
        if current_player_index == len(self.players_order) - 1:
            shuffle(self.players_order)
            self.current_player = self.players_order[0]
        else:
            self.current_player = self.players_order[(current_player_index + 1)]

        return state, action, reward, next_state

    def play(self):
        """ Runs gameplay until the game is over, then scores bonus Blocks.
        """

        self.setup()

        # Runs gameplay until only the base Blocks remain
        while not self.game_over:
            # Prints the current game state
            self.pretty_print()

            # Current player evaluates legal moves and selects the optimal (x,y) position
            move = self.players[self.current_player].evaluate_moves(self.board, self.legal_moves, self.players)

            # Applies the move that the player chose
            self.make_move(move)

            # If only the base Blocks remain, terminate the game
            if self.blocks_left == self.depth:
                self.game_over = True
            if len(self.legal_moves) == 0:
                self.game_over = True

            # Updates legal moves given the player's move choices
            self.update_legal_moves(move)

            # Re-randomize player order if necessary, otherwise increment player
            current_player_index = self.players_order.index(self.current_player)
            if current_player_index == len(self.players_order) - 1:
                shuffle(self.players_order)
                self.current_player = self.players_order[0]
            else:
                self.current_player = self.players_order[(current_player_index + 1)]

        # Prints the board
        self.vprint()
        self.pretty_print_board()

        # Scores bonus blocks
        self.score_bonus_blocks()

        # Prints the endgame and winner
        return self.pretty_print_for_end()

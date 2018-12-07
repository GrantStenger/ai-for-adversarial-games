class BoardTree:

    def __init__(self, game, board, player_to_move, depth_to_search, current_depth = 0, position_value = None, move_to_make = None):
        # print("__init__")
        # print()
        self.current_depth = current_depth
        self.depth_to_search = depth_to_search
        self.board = board
        self.player_to_move = player_to_move
        self.game = game
        self.position_value = position_value
        self.move_to_make = move_to_make
        self.children = []

        print(" " * self.current_depth, "self.current_depth", self.current_depth)
        print(" " * self.current_depth, "self.depth_to_search", self.depth_to_search)
        print(" " * self.current_depth, "self.board")
        game.print_board(self.board)
        print(" " * self.current_depth, "self.player_to_move", self.player_to_move)
        print(" " * self.current_depth, "self.position_value", self.position_value)
        print(" " * self.current_depth, "self.move_to_make", self.move_to_make)
        print()
        print()
        print()


        # If current depth is less than total depth to search, go deeper.
        if self.current_depth < self.depth_to_search and position_value == None:
            self.get_children()

        # for child in self.children:
        #     print("child.position_value, self.move_to_make:", child.position_value, self.move_to_make)
        self.get_best_move()
        # for child in self.children:
        #     print("child.position_value, self.move_to_make:", child.position_value, self.move_to_make)


    def get_children(self):
        # print("get_children")

        # Find and store all children nodes with legal moves
        children = []

        # Check each possible move and add each one to the list of children
        for column in range(self.game.columns):

            # First, update the imaginary board
            imaginary_board = [row[:] for row in self.board]
            imaginary_player_to_move = self.player_to_move

            valid_move = self.game.move(column, imaginary_board, player_to_move = imaginary_player_to_move)
            if valid_move:

                # Check if this move is winning
                # (check_board will return 1 if player 1 wins and -1 if player 2 wins)
                move_value = self.game.check_board(imaginary_board, imaginary = True)

                # If the move is either a tie or a win, store this value, else explore deeper
                if move_value != None:

                    # Switch which player's turn it is
                    imaginary_player_to_move = self.switch_player(imaginary_player_to_move)

                    # Add the move and value as children of the current node
                    new_node = BoardTree(self.game,
                                         imaginary_board,
                                         imaginary_player_to_move,
                                         self.depth_to_search,
                                         self.current_depth+1,
                                         position_value = move_value,
                                         move_to_make = column + 1
                                        )

                    if move_value == 1 and imaginary_player_to_move == self.game.player2:
                        children = [new_node]
                        return
                    elif move_value == -1 and imaginary_player_to_move == self.game.player1:
                        children = [new_node]
                        return

                    children.append(new_node)
                else:
                    # Switch which player's turn it is
                    imaginary_player_to_move = self.switch_player(imaginary_player_to_move)

                    new_node = BoardTree(self.game, imaginary_board, imaginary_player_to_move, self.depth_to_search, self.current_depth+1)
                    if self.current_depth + 1 == self.depth_to_search:
                        new_node.set_position_val(move_value)
                        new_node.set_move_to_make(column + 1)
                    children.append(new_node.get_best_move())

        self.children = children

    def set_position_val(self, move_value):
        # print("set_position_val(self, move_value)", move_value)
        self.position_value = move_value

    def set_move_to_make(self, move):
        # print("set_move_to_make(self, move)", move)
        self.move_to_make = move

    def switch_player(self, player):
        if player == self.game.player1:
            return self.game.player2
        else:
            return self.game.player1

    def get_best_move(self):
        # print("get_best_move")
        # print("self.current_depth", self.current_depth)
        # print("self.depth_to_search", self.depth_to_search)
        # print("self.board", self.board)
        # print("self.player_to_move", self.player_to_move)
        # print("self.game", self.game)
        # print("self.position_value", self.position_value)
        # print("self.move_to_make", self.move_to_make)

        if self.current_depth == self.depth_to_search:
            # print("here", self.position_value)
            return self

        if self.children == []:
            return self

        if self.player_to_move == self.game.player1:
            # print("HHHHHHHHHHHHHHHEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRREEEEEEEEEE1")
            # print(self.current_depth)
            for child in self.children:
                # print("child.position_value", child.position_value)
                if child.position_value == 1:
                    self.position_value = child.position_value
                    self.move_to_make = child.move_to_make
                    return child
            for child in self.children:
                # print("child.position_value", child.position_value)
                if child.position_value == 0:
                    self.position_value = child.position_value
                    self.move_to_make = child.move_to_make
                    return child
            for child in self.children:
                # print("child.position_value", child.position_value)
                if child.position_value == None:
                    self.position_value = child.position_value
                    self.move_to_make = child.move_to_make
                    return child
            for child in self.children:
                # print("child.position_value", child.position_value)
                if child.position_value == -1:
                    self.position_value = child.position_value
                    self.move_to_make = child.move_to_make
                    return child
        else:
            # print("HHHHHHHHHHHHHHHEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRREEEEEEEEEE2")
            # print(self.current_depth)
            for child in self.children:
                # print("child.position_value", child.position_value)
                if child.position_value == -1:
                    self.position_value = child.position_value
                    self.move_to_make = child.move_to_make
                    return child
            for child in self.children:
                # print("child.position_value", child.position_value)
                if child.position_value == 0:
                    self.position_value = child.position_value
                    self.move_to_make = child.move_to_make
                    return child
            for child in self.children:
                # print("child.position_value", child.position_value)
                if child.position_value == None:
                    self.position_value = child.position_value
                    self.move_to_make = child.move_to_make
                    return child
            for child in self.children:
                # print("child.position_value", child.position_value)
                if child.position_value == 1:
                    self.position_value = child.position_value
                    self.move_to_make = child.move_to_make
                    return child

    def print_tree(self):
        for i in range(self.current_depth):
            print("", end=" ")
        print("position_value, move_to_make:", self.position_value, self.move_to_make)
        for child in self.children:
            child.print_tree()

from collections import deque
import numpy as np
import torch

from MoveNet import MoveNet


class Game:
    def __init__(self, SIZE):
        self.SIZE = SIZE
        self.score = 0
        self.moves = 100
        self.dead = False
        self.snake = deque()
        self.snake.appendleft((np.random.randint(SIZE), np.random.randint(SIZE)))
        self.generate_food()
        print("Food: " + str(self.food))

        self.moveNet = MoveNet(SIZE)

    def generate_food(self):
        self.food = (np.random.randint(self.SIZE), np.random.randint(self.SIZE))
        if self.food in self.snake:
            self.generate_food()

    def neural_move(self):
        board = [[0] * self.SIZE for i in range(self.SIZE)]
        board[self.food[0]][self.food[1]] = 1
        for node in self.snake:
            board[node[0]][node[1]] = 2
        board[self.snake[0][0]][self.snake[0][1]] = 3
        print(board)
        board = np.asarray(board)
        print(board)
        board = board.flatten()
        print(board)
        board = torch.from_numpy(board)
        print(board)

        last_head_pos = self.snake[0]

        if len(self.snake) > 1:
            neck_pos = self.snake[1]
            next_head = self.snake[1]
            while next_head == neck_pos:
                pass
                next_head = self.moveNet.forward(board)
        else:
            pass
            next_head = self.moveNet.forward(board) 

        self.snake.pop()
        self.snake.appendleft(next_head)
        
        if self.SIZE in self.snake[0] or -1 in self.snake[0]:
            self.dead = True
        if self.snake.count(self.snake[0]) > 1:
            self.dead = True

        if self.snake[0] == self.food:
            self.eat(last_head_pos)

        self.moves -= 1


    def random_move(self):
        last_head_pos = self.snake[0]

        if len(self.snake) > 1:
            neck_pos = self.snake[1]
            next_head = self.snake[1]
            while next_head == neck_pos:
                next_head = self.pick_move(last_head_pos)
        else:
            next_head = self.pick_move(last_head_pos)

        self.snake.pop()
        self.snake.appendleft(next_head)
        
        if self.SIZE in self.snake[0] or -1 in self.snake[0]:
            self.dead = True
        if self.snake.count(self.snake[0]) > 1:
            self.dead = True

        if self.snake[0] == self.food:
            self.eat(last_head_pos)

        self.moves -= 1

    def pick_move(self, last_head_pos):
        move = np.random.random()
        if move < 0.25:
            next_head = (last_head_pos[0] + 1, last_head_pos[1])
        elif move < 0.5:
            next_head = (last_head_pos[0] - 1, last_head_pos[1])
        elif move < 0.75:
            next_head = (last_head_pos[0], last_head_pos[1] + 1)
        else:
            next_head = (last_head_pos[0], last_head_pos[1] - 1)
        return next_head

    def eat(self, last_head_pos):
        if (last_head_pos[0] + 1, last_head_pos[1]) == self.snake[0]:
            self.snake.append((self.snake[-1][0] - 1, self.snake[-1][1]))
        elif (last_head_pos[0] - 1, last_head_pos[1]) == self.snake[0]:
            self.snake.append((self.snake[-1][0] + 1, self.snake[-1][1]))
        elif (last_head_pos[0], last_head_pos[1] + 1) == self.snake[0]:
            self.snake.append((self.snake[-1][0], self.snake[-1][1] - 1))
        else:
            self.snake.append((self.snake[-1][0], self.snake[-1][1] + 1))

        self.generate_food()

        print("Eaten!")
        self.score += 1
        self.moves += 100

    def play(self):
        while not (self.dead or self.moves == 0):
            print(self.snake[0])
            self.neural_move()
        if self.dead:
            print("Dead!")
        else:
            print("Moves ran out!")
        print("Score: " + str(self.score))

def main():
    game = Game(10)
    game.play()

if __name__ == "__main__":
    main()

import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
from collections import namedtuple

class DQN(nn.Module):
    """ A Deep Q-Network for intelligently playing Pyramix.
    """

    def __init__(self, DEPTH, NUM_COLORS):
        """ Initializes a Deep Q-Network.
        """

        super(DQN, self).__init__()
        self.depth = DEPTH
        self.num_colors = NUM_COLORS

        # First convolution and batch norm
        self.conv1 = nn.Conv2d(3 * NUM_COLORS, 6 * NUM_COLORS, 4)
        self.bn1 = nn.BatchNorm2d(6 * NUM_COLORS)
        
        # Second convolution and batch norm
        self.conv2 = nn.Conv2d(6 * NUM_COLORS, 12 * NUM_COLORS, 4)
        self.bn2 = nn.BatchNorm2d(12 * NUM_COLORS)

        # Linear layer
        self.head = nn.Linear(12 * NUM_COLORS * (DEPTH - 6) * (DEPTH - 6) , DEPTH * DEPTH)

    def forward(self, X):
        """ A forward pass of the Deep Q-Network.
        """
        
        conv1_result = F.relu(self.bn1(self.conv1(X)))
        conv2_result = F.relu(self.bn2(self.conv2(conv1_result)))
        head_result = torch.sigmoid(self.head(conv2_result.view(conv2_result.size(0), -1)))
        return head_result

    def game_matrix_to_tensor(self, matrix):
        """ Converts Game matrix to PyTorch Tensor
        """
        
        # Changes type from Numpy array to PyTorch Tensor
        input = torch.from_numpy(matrix)

        # Adds a batch dimension
        input = input[None, :, :, :]

        # Converts dtype to float
        return(input.float())

Transition = namedtuple("Transition", ("state", "action", "reward", "next_state"))
class QTable():
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
        self.position = 0
        
    def push(self, *args):
        """ Saves a Transition to the QTable.
        """
    
        if len(self.memory) < self.capacity:
            self.memory.append(None)
        self.memory[self.position] = Transition(*args)
        self.position = (self.position + 1) % self.capacity
        
    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)


import torch
import torch.nn.functional as F
from torch import nn
import math

class MoveNet(nn.Module):
    def __init__(self, SIZE):
        super().__init__()
        self.INPUT_DIM = SIZE * SIZE
        self.H1_DIM = math.floor(0.6 * SIZE)
        self.H2_DIM = math.floor(0.2 * SIZE)
        self.OUTPUT_DIM = 4

        self.linear1 = nn.Linear(self.INPUT_DIM, self.H1_DIM)
        self.linear2 = nn.Linear(self.H1_DIM, self.H2_DIM)
        self.linear3 = nn.Linear(self.H2_DIM, self.OUTPUT_DIM)

    def forward(self, X):
        hidden1 = F.relu(self.linear1(X))
        hidden2 = F.relu(self.linear2(hidden1))
        output = F.relu(self.linear3(hidden2))

        return output

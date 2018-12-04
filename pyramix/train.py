import random
import math
import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim
import statistics as stat

from DQN import DQN
from DQN import QTable
from DQN import Transition
from Game import Game
from players.Neural import Neural

BATCH_SIZE = 1
GAMMA = 0.999
EPS_START = 1.0
EPS_END = 0.01
EPS_DECAY = 10000 
        
DEPTH = 9
NUM_COLORS = 3

dqn = DQN(DEPTH, NUM_COLORS)

optimizer = optim.Adam(dqn.parameters())
qtable = QTable(100000)

steps_done = 0
vprint = lambda *a, **k: None

def select_action(game):
    global steps_done
    
    eps_threshold = EPS_END + (EPS_START - EPS_END) * math.exp(-1. * steps_done / EPS_DECAY)

    steps_done += 1
    
    if random.random() > eps_threshold:
        game_matrix = game.export_matrix_for_cnn()
    
        tensor = dqn.game_matrix_to_tensor(game_matrix)
        inference = dqn(tensor)

        #print(inference)

        index = inference.max(1)[1]
        row = int(index / DEPTH)
        col = np.asscalar((index % (row + 1)).numpy())
        move_tuple = (row, col)

        return torch.tensor([index], dtype=torch.float32), move_tuple
    else:
        #print("rand")
        #random_action = torch.tensor([random.randint(0, DEPTH * DEPTH)], dtype = torch.float32)
        #index = np.asscalar(random_action.numpy())
        #row = int(index / DEPTH)
        #col = int(index % (row + 1))
        #random_move = (row, col)
        random_move = game.legal_moves[random.randint(0, len(game.legal_moves) - 1)]
        index = DEPTH * random_move[0]
        random_action = torch.tensor([index], dtype=torch.float32)
        return random_action, random_move

def compute_td_loss():
    if len(qtable) < BATCH_SIZE:
        return

    transitions = qtable.sample(BATCH_SIZE)

    batch = Transition(*zip(*transitions))
    state = batch.state[0]
    action = batch.action[0]
    reward = batch.reward[0]
    next_state = batch.next_state[0]

    q_values = dqn(state)
    q_values_next = dqn(next_state)

    # Can do because batch size is one
    q_value = q_values
    q_value_next = q_values_next
    #q_value = q_values.gather(1, action).squeeze(1)
    #q_value_next = q_values_next.max(1)[0]

    expected_q_value = reward + GAMMA * q_value_next

    loss = (q_value - expected_q_value).pow(2).mean()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()   

    return loss

EPOCHS = 1000000
for epoch in range(EPOCHS):
    players = [Neural(dqn), Neural(dqn)]

    game = Game(players=players, depth=DEPTH, num_colors=NUM_COLORS, vprint=vprint)
    game.setup()

    rewards = []
    losses = []

    while True:
        # Select an action
        action, move = select_action(game)

        # Perform the action
        state, _, reward, next_state = game.step(move)

        rewards.append(reward)

        # Convert inferences to tensors
        state = dqn.game_matrix_to_tensor(state)
        reward = torch.tensor(torch.from_numpy(np.asarray(reward)), dtype=torch.float32)
        next_state = dqn.game_matrix_to_tensor(next_state)

        # Store the transition in memory
        qtable.push(state, action, reward, next_state)

        # Perform one step of the optimization
        loss = np.asscalar(compute_td_loss().detach().numpy())

        losses.append(loss)
        
        if game.game_over:
            break

    print("Mean loss for epoch " + str(epoch) + ": " + str(stat.mean(losses)))
    print("Mean reward for epoch " + str(epoch) + ": " + str(stat.mean(rewards)))


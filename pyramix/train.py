import random
import math
import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim

from DQN import DQN
from DQN import QTable
from DQN import Transition
from Game import Game
from players.Neural import Neural

BATCH_SIZE = 1
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 200
TARGET_UPDATE = 5
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

policy_net = DQN(15, 4).to(DEVICE)
target_net = DQN(15, 4).to(DEVICE)
target_net.load_state_dict(policy_net.state_dict())
target_net.eval()

optimizer = optim.RMSprop(policy_net.parameters())
qtable = QTable(10000)
steps_done = 0

vprint = lambda *a, **k: None

def select_action(game):
    global steps_done
    
    eps_threshold = EPS_END + (EPS_START - EPS_END) * math.exp(-1. * steps_done / EPS_DECAY)
    
    steps_done += 1

    random_move = game.legal_moves[random.randint(0, len(game.legal_moves) - 1)]

    if random.random() > eps_threshold:
        with torch.no_grad():
            game_matrix = game.export_matrix_for_cnn()
            
            tensor = policy_net.game_matrix_to_tensor(game_matrix)
            inference = policy_net(tensor)

            move_tensor = inference.clone()
            move_matrix = move_tensor.detach().numpy()

            index = np.argmax(move_matrix)
            row = int(index / game.depth)
            move_tuple = (row, index % (row + 1))

            if move_tuple in game.legal_moves:
                return torch.tensor([index]), move_tuple
            else:
                return torch.tensor([index]), random_move
    else:
        print("rand")
        return torch.tensor([random.randint(0, 225)]), random_move

# Basically copied from the pytorch tutorial
def optimize_model():
    if len(qtable) < BATCH_SIZE:
        return

    transitions = qtable.sample(BATCH_SIZE)

    batch = Transition(*zip(*transitions))
 
    non_final_mask = torch.tensor(tuple(map(lambda s: s is not None, batch.next_state)), device=DEVICE, dtype=torch.uint8)
    non_final_next_states = torch.cat([s for s in batch.next_state if s is not None])

    state_batch = torch.cat(batch.state)
    action_batch = torch.cat(batch.action)
    reward_batch = torch.cat(batch.reward)

    state_action_values = policy_net(state_batch).gather(1, action_batch.long())

    next_state_values = torch.zeros(BATCH_SIZE, device=DEVICE)
    next_state_values[non_final_mask] = target_net(non_final_next_states).max(1)[0].detach()

    expected_state_action_values = (next_state_values.long() * GAMMA) + reward_batch

    loss = F.smooth_l1_loss(state_action_values, expected_state_action_values.unsqueeze(1).float())

    optimizer.zero_grad()
    loss.backward()
    for param in policy_net.parameters():
        param.grad.data.clamp_(-1, 1)
    optimizer.step()   

EPOCHS = 20
for epoch in range(EPOCHS):
    # Somehow need to persist weights
    players = [Neural(policy_net), Neural(policy_net), Neural(policy_net)]

    game = Game(players=players, depth=15, num_colors=4, vprint=vprint)
    game.setup()

    while True:
        action, move = select_action(game)

        # Select and perform an action
        state, _, reward, next_state = game.step(move)

        state = policy_net.game_matrix_to_tensor(state)
        reward = torch.tensor(torch.from_numpy(np.asarray(reward)))
        next_state = policy_net.game_matrix_to_tensor(next_state)

        # Store the transition in memory
        qtable.push(state, action, reward, next_state)

        # Perform one step of the optimization (on the target network)
        optimize_model()

        if game.game_over:
            break

    # Update the target network
    if epoch % TARGET_UPDATE == 0:
        target_net.load_state_dict(policy_net.state_dict()) 

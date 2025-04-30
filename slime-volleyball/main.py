import slimevolleygym
import random
import numpy as np

# Define the action space (all possible combinations)
ACTION_SPACE = [
    [0, 0, 0],  # no action
    [1, 0, 0],  # left
    [0, 1, 0],  # right
    [0, 0, 1],  # jump
    [1, 0, 1],  # left + jump
    [0, 1, 1],  # right + jump
    [1, 1, 0],  # left + right (weird but included)
    [1, 1, 1],  # all actions
]

# Simple heuristic to evaluate a state
def evaluate_state(state):
    """
    Encourages the agent to be close to the ball and near the net (center).
    Indexes:
    state[0]: ball_x
    state[2]: agent_x
    """
    ball_x = state[0]
    agent_x = state[2]
    return -abs(agent_x - ball_x) - abs(agent_x - 0.5)

# Simulate a step by replaying the action history
def simulate_step_from_history(action_history, action1, action2):
    sim_env = slimevolleygym.SlimeVolleyEnv()
    sim_env.reset()
    for a1, a2 in action_history:
        # Flatten actions and pass to step
        sim_env.step([a1[0], a1[1], a1[2], a2[0], a2[1], a2[2]])  # Pass flattened actions
    # Simulate the final step
    obs, _, _, _ = sim_env.step([action1[0], action1[1], action1[2], action2[0], action2[1], action2[2]])
    return obs

# Minimax with alpha-beta pruning
def minimax(env, depth, alpha, beta, maximizing_player, action_history):
    if depth == 0:
        # Simulate a step with no actions and evaluate the state
        obs = simulate_step_from_history(action_history, [0, 0, 0], [0, 0, 0])
        return evaluate_state(obs), None

    best_action = None

    if maximizing_player:
        max_eval = -float('inf')
        for action in ACTION_SPACE:
            opponent_action = random.choice(ACTION_SPACE)
            new_history = action_history + [(action, opponent_action)]
            eval_score, _ = minimax(env, depth - 1, alpha, beta, False, new_history)
            if eval_score > max_eval:
                max_eval = eval_score
                best_action = action
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_action
    else:
        min_eval = float('inf')
        for action in ACTION_SPACE:
            opponent_action = random.choice(ACTION_SPACE)
            new_history = action_history + [(opponent_action, action)]
            eval_score, _ = minimax(env, depth - 1, alpha, beta, True, new_history)
            if eval_score < min_eval:
                min_eval = eval_score
                best_action = action
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_action

# Use minimax to decide the best action
def get_minimax_action(env, action_history, depth=2):
    _, best_action = minimax(env, depth, -float('inf'), float('inf'), True, action_history)
    return best_action

# Main game loop
def play_game():
    env = slimevolleygym.SlimeVolleyEnv()
    obs = env.reset()
    done = False
    action_history = []
    frame_count = 0
    depth = 2  # Keep depth small for efficiency

    while not done:
        frame_count += 1
        print(f"\n🎮 Frame {frame_count}")

        # Get action from minimax AI
        action1 = get_minimax_action(env, action_history, depth)

        # Random action for opponent
        action2 = random.choice(ACTION_SPACE)

        # Flatten the actions and take a step
        obs, reward, done, _ = env.step([action1[0], action1[1], action1[2], action2[0], action2[1], action2[2]])
        action_history.append((action1, action2))

        print(f"Agent Action: {action1}, Opponent Action: {action2}")
        print(f"Observation: {obs}")
        print(f"Reward: {reward}")

    print("🏁 Game Over!")

# ✅ Corrected main block
if __name__ == "__main__":
    play_game()
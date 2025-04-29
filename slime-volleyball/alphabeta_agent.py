import numpy as np
from eval import evaluate

def alphabeta(env, state, depth, alpha, beta, maximizing, action_space):
    if depth == 0:
        return evaluate(state), None

    best_action = None
    if maximizing:
        value = float('-inf')
        for action in action_space:
            next_state = simulate_step(env, state, action, None)
            eval, _ = alphabeta(env, next_state, depth - 1, alpha, beta, False, action_space)
            if eval > value:
                value = eval
                best_action = action
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, best_action
    else:
        value = float('inf')
        for action in action_space:
            next_state = simulate_step(env, state, None, action)
            eval, _ = alphabeta(env, next_state, depth - 1, alpha, beta, True, action_space)
            if eval < value:
                value = eval
                best_action = action
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_action

def get_alphabeta_action(env, obs, depth, action_space):
    _, action = alphabeta(env, obs, depth, float('-inf'), float('inf'), False, action_space)
    return action

def simulate_step(env, state, action1, action2):
    sim_env = slimevolleygym.SlimeVolleyEnv()
    sim_env.reset()
    sim_env.set_state(state)

    obs, _, _, _ = sim_env.step((action1 or np.array([0, 0, 0]), action2 or np.array([0, 0, 0])))
    return obs


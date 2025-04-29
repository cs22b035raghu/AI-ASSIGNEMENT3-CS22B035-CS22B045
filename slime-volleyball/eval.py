def evaluate(obs):
    agent_y = obs[1]     # y-position of the agent
    ball_x = obs[4]      # x-position of the ball
    ball_y = obs[5]      # y-position of the ball

    score = ball_y * 10 - abs(ball_x - 0) * 5 + agent_y
    return score


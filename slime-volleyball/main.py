import slimevolleygym
from minimax_agent import get_minimax_action

def play_game():
    env = slimevolleygym.SlimeVolleyEnv()
    obs = env.reset()  # Initialize the environment
    done = False
    depth = 3  # Minimax depth (can adjust this based on your needs)
    
    while not done:
        # Call minimax to get the next action
        action1 = get_minimax_action(env, obs, depth, env.action_space)
        
        # Take the step in the environment
        obs, reward, done, info = env.step([action1, env.action_space.sample()])
        
        # Render the environment (optional)
        env.render()
        
    env.close()

if __name__ == "__main__":
    play_game()

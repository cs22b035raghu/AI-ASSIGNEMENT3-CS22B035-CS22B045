🏐 SlimeVolley Minimax Agent
This project implements an AI agent that plays SlimeVolleyGym, a simple 2D volleyball game. The AI uses the Minimax algorithm with Alpha-Beta pruning to determine its next action, while playing against a random opponent.

📌 Features
✅ Minimax search with alpha-beta pruning to explore possible future game states.

✅ Custom heuristic evaluation function that rewards proximity to the ball and center of the court.

✅ A set of 8 discrete actions (combinations of movement and jumping).

✅ Turn-based simulation for decision-making.

✅ Simple gameplay loop with frame-by-frame output.

🤖 Algorithm Used
Yes, this project does use Minimax with Alpha-Beta pruning. Here's how:

The AI recursively explores possible future actions using the Minimax algorithm.

Alpha-beta pruning is used to eliminate branches that cannot affect the final decision, improving efficiency.

At each leaf node, a heuristic evaluation function scores the game state based on proximity to the ball and the center (net).

Install Dependencies
Use requirements.txt:

pip install -r requirements.txt


🧠 Action Space
The agent selects from the following discrete actions:

scss
Copy
Edit
[0, 0, 0]  # No action
[1, 0, 0]  # Move left
[0, 1, 0]  # Move right
[0, 0, 1]  # Jump
[1, 0, 1]  # Left + Jump
[0, 1, 1]  # Right + Jump
[1, 1, 0]  # Left + Right (not physically meaningful)
[1, 1, 1]  # All actions


♟️ Chess AI with Minimax & Alpha-Beta Pruning

chess/
├── alphabeta_bot.py
├── chess_game.mp4
├── evaluation.py
├── main.py
├── minimax_bot.py
├── requirements.txt

This is a Python-based Chess AI agent that plays chess using the Minimax algorithm with optional Alpha-Beta pruning, supporting simple board evaluation. It plays autonomously and can generate match videos (chess_game.mp4).

📁 File Overview

File	Description
main.py	Entry point — runs the chess game
alphabeta_bot.py	AI logic using Alpha-Beta pruning
minimax_bot.py	Alternative AI logic using plain Minimax (no pruning)
evaluation.py	Evaluation functions (piece value heuristics)
chess_game.mp4	Video recording of a sample game
requirements.txt	Dependencies for the project
🛠️ Installation
1. Clone the repository

git clone <your-repo-url>
cd chess
2. Set up virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate
3. Install dependencies

pip install -r requirements.txt
▶️ Run the AI Game
To play a full AI-vs-AI game:

python main.py
Example output:


Turn 1: White (Minimax) plays e2e4
Turn 2: Black (AlphaBeta) plays e7e5
...
Game result: 1/2-1/2


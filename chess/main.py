import chess
import time
from minimax_bot import get_minimax_move
from alphabeta_bot import get_alphabeta_move

def play_game(depth=3):
    board = chess.Board()
    turn = 0  # 0: Minimax, 1: AlphaBeta

    while not board.is_game_over():
        print(board, '\n')
        if turn == 0:
            print("Minimax is thinking...")
            start = time.time()
            move = get_minimax_move(board, depth, chess.WHITE)
            print("Minimax played:", move, "in", round(time.time() - start, 2), "s")
        else:
            print("AlphaBeta is thinking...")
            start = time.time()
            move = get_alphabeta_move(board, depth, chess.BLACK)
            print("AlphaBeta played:", move, "in", round(time.time() - start, 2), "s")

        board.push(move)
        turn = 1 - turn

    print("\nGame over!")
    print(board.result())

if __name__ == "__main__":
    play_game(depth=3)


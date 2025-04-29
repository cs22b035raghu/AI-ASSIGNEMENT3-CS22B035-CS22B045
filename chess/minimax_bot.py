import chess
from evaluation import evaluate

def minimax(board, depth, maximizing, color):
    if depth == 0 or board.is_game_over():
        return evaluate(board, color), None

    best_move = None
    if maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, False, color)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, True, color)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

def get_minimax_move(board, depth, color):
    _, move = minimax(board, depth, board.turn == color, color)
    return move


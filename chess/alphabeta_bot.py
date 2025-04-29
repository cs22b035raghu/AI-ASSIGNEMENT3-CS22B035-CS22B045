import chess
from evaluation import evaluate

def alphabeta(board, depth, alpha, beta, maximizing, color):
    if depth == 0 or board.is_game_over():
        return evaluate(board, color), None

    best_move = None
    if maximizing:
        value = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = alphabeta(board, depth - 1, alpha, beta, False, color)
            board.pop()
            if eval > value:
                value = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return value, best_move
    else:
        value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = alphabeta(board, depth - 1, alpha, beta, True, color)
            board.pop()
            if eval < value:
                value = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return value, best_move

def get_alphabeta_move(board, depth, color):
    _, move = alphabeta(board, depth, float('-inf'), float('inf'), board.turn == color, color)
    return move


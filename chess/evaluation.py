import chess

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

def evaluate(board, player_color):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = PIECE_VALUES[piece.piece_type]
            score += value if piece.color == player_color else -value

    # Mobility
    mobility = len(list(board.legal_moves))
    score += 0.1 * mobility if board.turn == player_color else -0.1 * mobility

    # Repetition penalty
    if len(board.move_stack) >= 4:
        w1 = board.move_stack[-4]
        b2 = board.move_stack[-3]
        w3 = board.move_stack[-2]
        b4 = board.move_stack[-1]
        if (w1.from_square == w3.to_square and w1.to_square == w3.from_square and
            b2.from_square == b4.to_square and b2.to_square == b4.from_square):
            score -= 500

    return score


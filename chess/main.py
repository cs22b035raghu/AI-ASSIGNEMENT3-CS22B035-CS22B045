import chess
import chess.svg
import numpy as np
import time
import cv2
from minimax_bot import get_minimax_move
from alphabeta_bot import get_alphabeta_move
from PIL import Image
import cairosvg
from io import BytesIO

# Function to generate a chessboard image from a given board state
def board_to_image(board):
    # Generate the SVG of the current board
    svg = chess.svg.board(board)
    
    # Convert the SVG to PNG using cairosvg
    png_data = cairosvg.svg2png(bytestring=svg.encode("utf-8"))
    
    # Open the PNG data with PIL
    img = Image.open(BytesIO(png_data))
    return img

def play_game(depth=3, video_filename="chess_game.mp4"):
    board = chess.Board()
    turn = 0  # 0: Minimax, 1: AlphaBeta
    frames = []  # List to store the board images for video creation
    
    # Set up video writer
    frame_width, frame_height = 600, 600  # Adjust the size as needed
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for .mp4 format
    out = cv2.VideoWriter(video_filename, fourcc, 1, (frame_width, frame_height))  # 1 frame per second
    
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

        # Convert the board to an image and add to frames
        img = board_to_image(board)
        img = img.resize((frame_width, frame_height))  # Resize to fit video frame
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
        frames.append(img)
        
        board.push(move)
        turn = 1 - turn

    # Write the frames to the video file
    for frame in frames:
        out.write(frame)

    out.release()  # Finalize the video file
    print("\nGame over!")
    print(board.result())

if __name__ == "__main__":
    play_game(depth=3)

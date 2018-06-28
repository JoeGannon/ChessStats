import chess.pgn
import math

pgn = open("test-game.pgn")

game = chess.pgn.read_game(pgn)

board = game.board()

for i, move in enumerate(game.main_line()):

    if (i % 2 == 0):
        print("turn " + str(math.ceil((i + 1) / 2)))         
    
    print (board.san(move))
    board.push(move)                      
    print (board.fen())
    print ("")
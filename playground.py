import chess.pgn
import math
import json

pgn = open("test-game.pgn")

game = chess.pgn.read_game(pgn)

board = game.board()


with open("openings.json") as json_file:
    openings = json.load(json_file)


for o in openings:
    if o['n'] == "Amar Gambit":
        print(o)
        
"""
for i, move in enumerate(game.main_line()):

    if (i % 2 == 0):
        print("turn " + str(math.ceil((i + 1) / 2)))         
    
    print (board.san(move))
    board.push(move)                      
    print (board.fen())
    print ("")


def dumb():
    return "dumb"   
"""
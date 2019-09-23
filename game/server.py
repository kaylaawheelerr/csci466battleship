import urllib
import re
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO



#default file paths being used
personal_board = r"/Users/cole.sluggett/Documents/git/csci466battleship/game/own_board.txt"
enemy_board = r"/Users/cole.sluggett/Documents/git/csci466battleship/game/opponent_board.txt"


#Counting a hit at the spot on the board if it is there
def countHit(file, xCoord, yCoord):
    board = open(file, "r")
    s = board.readlines()
    board.close()
    return s[yCoord][xCoord]


#checks the entire board for hits to see if there is a winner
def countBoard(file):
    numHits = 0
    for i in range(10):
        for j in range(10):
            hit = countHit(file, i, j)
            if hit == 'X' or hit == 'O':
                numHits += 1
    return numHits


#A simple print board method
def print_board(file):
    board = open(file, "r")
    for i in board:
        print(i)
    board.close()
    return board

#Here will process the shot
def sunkTest(file,letterSpot):
    board = open(personal_board, "r")
    tempBoard = board.readlines()
    board.close()
    for i in range(10):
        for j in range(10):
            if str(tempBoard[i][j]) == letterSpot:
                return 0
    sunkShip = 'hit=1\&sink=' + letterSpot
    for i in range(10):
        for j in range(10):
            if tempBoard[i][j] != '_' and tempBoard[i][j] != 'X' and tempBoard[i][j] != 'O' and tempBoard[i][j] != 'O':
                return sunkShip.encode()
    return 420

def shotTaken(xCoord, yCoord):
    xCoord = int(xCoord)
    yCoord = int(yCoord)

    board = open(personal_board, "r")
    tempBoard = board.readlines()
    board.close()

    shot_board = open(enemy_board, "r")
    tempShotBoard = shot_board.readlines()
    shot_board.close()

    print("Attempted to fire here " + str(xCoord) + " " + str(yCoord))

    #This spot is a hit on a ship
    if tempBoard[yCoord][xCoord] != '_' and tempBoard[yCoord][xCoord] != 'X' and tempBoard[yCoord][xCoord] != 'O':
        print("looks like we got a hit!")
        letterSpot = str(tempBoard[yCoord][xCoord])
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord] + \
            "X" + tempBoard[yCoord][xCoord+1:]
        tempShotBoard[yCoord] = tempShotBoard[yCoord][0:xCoord] + \
            "X" + tempShotBoard[yCoord][xCoord+1:]
        board = open(personal_board, "w")
        shot_board = open(enemy_board, "w")

        for i in tempBoard:
            board.write(i)
        for i in tempShotBoard:
            shot_board.write(i)
        board.close()
        shot_board.close()
        sink = sunkTest(board,letterSpot)
        print_board(personal_board)
        if sink == 0:
            return 201
        return sink

    elif tempBoard[yCoord][xCoord] == "_":
        print("Shot and a miss!")
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord] + \
            "O" + tempBoard[yCoord][xCoord+1:]
        tempShotBoard[yCoord] = tempShotBoard[yCoord][0:xCoord] + \
            "O" + tempShotBoard[yCoord][xCoord+1:]
        board = open(personal_board, "w")
        shot_board = open(enemy_board, "w")

        for i in tempBoard:
            board.write(i)
        for i in tempShotBoard:
            shot_board.write(i)
        board.close()
        shot_board.close()
        print_board(personal_board)
        return 300

    else:
        return 350

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self): 
        content = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content)
        post_data = post_data.decode("utf-8")
        coords = re.findall(r'\d+', post_data)
        x = int(coords[0])
        y = int(coords[1])
        response = BytesIO()
        if x > -1 and x < 10 and y > -1 and y < 10:
            return_message = shotTaken(x,y)
            if type(return_message) != int:
                self.send_response(400)
                response.write(return_message)
                self.end_headers()
            else:
                self.send_response(return_message)
                self.end_headers()
        else:
            self.send_response(208)
            self.end_headers()
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

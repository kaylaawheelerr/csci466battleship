import urllib
import re
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


# def create_board(board_file):
#     f = open(board_file, "r")
#     if f.mode == 'r':
#         BOARD = f.read()
#         print(BOARD)


#default file paths being used
personal_board = r"/Users/christianmarquardt/Documents/GitHub/csci466battleship/game/own_board.txt"
enemy_board = r"/Users/christianmarquardt/Documents/GitHub/csci466battleship/enemy_board.txt"


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


def checkForInput(xCoord, yCoord):
    if xCoord > 9 and xCoord < 0 and yCoord > 9 and yCoord < 0:
        return [404, "HTTP Not Found"]
    else:
        return shotTaken(xCoord, yCoord)

#Here will process the shot
def sunkTest(file,letterSpot):
    board = open(personal_board, "r")
    tempBoard = board.readlines()
    board.close()
    for i in range(10):
        for j in range(10):
            if str(tempBoard[i][j]) == letterSpot:
                return 0
    sunkShip = str("hit=1\&sink=" + letterSpot)
    return sunkShip

def shotTaken(xCoord, yCoord):
    xCoord = int(xCoord)
    yCoord = int(yCoord)

    board = open(personal_board, "r")
    tempBoard = board.readlines()
    board.close()

    print("Attempted to fire here " + str(xCoord) + " " + str(yCoord))

    #This spot is a hit on a ship
    if tempBoard[yCoord][xCoord] != '_' and tempBoard[yCoord][xCoord] != 'X' and tempBoard[yCoord][xCoord] != 'O':
        print("looks like we got a hit!")
        letterSpot = str(tempBoard[yCoord][xCoord])
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord] + \
            "X" + tempBoard[yCoord][xCoord+1:]
        board = open(personal_board, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        sink = sunkTest(board,letterSpot)
        print_board(personal_board)
        if sink == "still alive":
            return 1
        return sink

    elif tempBoard[yCoord][xCoord] == "_":
        print("Shot and a miss!")
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord] + \
            "O" + tempBoard[yCoord][xCoord+1:]
        board = open(personal_board, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        print_board(personal_board)
        return 0

def create_board(board_file):
    f = open(board_file, "r")
    if f.mode == 'r':
        BOARD = (f.read())
        print(BOARD)
    return(BOARD)


def board_stringy(file):
    f = open(file, "r")
    print(f)
    board_string =str()
    for line in f:
        board_string += "<div class = 'grid-container'>"
        for character in line:
            board_string += "<div class = 'grid-item'>" + character + "</div>"
        board_string += "</div>"     
    board_string = str.encode(board_string)
    f.close()
    return(board_string)


#BOARD = create_board(sys.argv[2])
PORT = sys.argv[1]
#board_string = board_string(personal_board)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        board_string = board_stringy(personal_board)
        self.send_response(200)
        self.end_headers()
        self.send_header('Content-type' , "text/html")
        self.wfile.write(b"<html><style>.grid-container{display: flex;}.grid-item{width: 25px;}</style><body><h1 class = 'container'>"
            +board_string+ b"</h1></body></html>")

    def do_POST(self): 
        content = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content)
        post_data = post_data.decode("utf-8")
        coords = re.findall(r'\d+', post_data)
        x = int(coords[0])
        y = int(coords[1])
        return_message = checkForInput(x,y)
        if return_message == 0:
            self.send_response(300)
        elif return_message == 1:
            self.send_response(350)
        self.send_response(return_message)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()


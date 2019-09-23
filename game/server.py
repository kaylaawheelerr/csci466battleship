# Christian Marquardt and Dylan Lynn
# 9/23/3019
# CSCI446 
# PA1

import urllib
import re
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

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



#A middleman subfunction that determines if the coordinates being sent in are allowed to be used
def checkForInput(xCoord, yCoord):
    if xCoord > 9 and xCoord < 0 and yCoord > 9 and yCoord < 0:
        return [404, "HTTP Not Found"]
    else:

        #Processes the shot
        return shotTaken(xCoord, yCoord)

#Test to see if we sunk the ship or not and pass that through
def sunkTest(file,letterSpot):
    board = open(personal_board, "r")
    tempBoard = board.readlines()
    board.close()
    for i in range(10):
        for j in range(10):
            if str(tempBoard[i][j]) == letterSpot:
                return 1
    if letterSpot == 'C':
        return 201
    elif letterSpot == 'B':
        return 202
    elif letterSpot == 'R':
        return 203
    elif letterSpot == 'S':
        return 204
    elif letterSpot == 'D':
        return 205
    else:
        return 1


#This takes the shot coordinates and opens the file and replaces the string row
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

        #When we get a hit we want to check if we sunk the ship or not
        sink = sunkTest(board,letterSpot)
        print_board(personal_board)
        if sink == 1:
            return 1
        return sink

    #Here would be a miss and write a O on that spot
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

def boardWrite(file):
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


#The specific port we want to grab by typing onto the command line
PORT = sys.argv[1]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        board_string = boardWrite(personal_board)
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

        #For a miss
        if return_message == 0:
            self.send_response(300)

        #For a hit
        elif return_message == 1:
            self.send_response(200)
        
        #For sinking Carrier
        elif return_message == 201:
            self.send_response(201)
        
        #For sinking Battleship
        elif return_message == 202:
            self.send_response(202)
        
        #For sinking cRuiser
        elif return_message == 203:
            self.send_response(203)

        #For sinking Submarine
        elif return_message == 204:
            self.send_response(204)
        
        #For sinking Destroyer
        elif return_message == 205:
            self.send_response(205)

        self.send_response(return_message)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()


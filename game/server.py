# Christian Marquardt and Dylan Lynn
# 9/23/3019
# CSCI446 
# PA1

import urllib
import re
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
from io import BytesIO

#default file paths being used

if sys.argv[2] == "own_board.txt":
    personal_board = "own_board.txt"
    enemy_board = "enemy_board.txt"
    shots_taken = "shots_taken.txt"
else:
    personal_board = "enemy_board.txt"
    enemy_board = "own_board.txt"
    shots_taken = "opp_shots_taken.txt"

PORT = int(sys.argv[1])

if PORT == 8000:
    PORT =8000
    PORT2= 8001
else:
    PORT = 8001
    PORT2 = 8000


def checkWin(file):
    countShipLives = 0
    board = open(file, "r")
    tempBoard = board.readlines()
    board.close()
    for i in range(10):
        for j in range(10):
            checker = str(tempBoard[i][j])
            if checker != "_" and checker != "O" and checker != "X":
                countShipLives += 1
    if countShipLives == 0:
        return "win"
    else:
       return "keep going"


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
    board = open(enemy_board, "r")
    tempBoard = board.readlines()
    board.close()
    for i in range(10):
        for j in range(10):
            if str(tempBoard[i][j]) == letterSpot:
                return 0
    return 1

# TODO
# 1st should update own board and enemy shot board. depending on which port was supplied.
#This takes the shot coordinates and opens the file and replaces the string row
def shotTaken(xCoord, yCoord):
    myobj = { 'x' : xCoord , 'y' : yCoord , 'z' : 1}
    url = 'http://localhost:'+str(PORT2)
    requests.post(url,myobj)
    xCoord = int(xCoord)
    yCoord = int(yCoord)
    
    board = open(personal_board, "r")
    tempBoard = board.readlines()
    board.close()

    print("Attempted to fire here " + str(xCoord) + " " + str(yCoord))
    if tempBoard[yCoord][xCoord] != '_' and tempBoard[yCoord][xCoord] != 'X' and tempBoard[yCoord][xCoord] != 'O': 
        letterSpot = str(tempBoard[yCoord][xCoord])
        print("looks like we got a hit!")
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord] + \
            "X" + tempBoard[yCoord][xCoord+1:]

        board = open(personal_board, "w")


        for i in tempBoard:
            board.write(i)
        board.close()
       

        #When we get a hit we want to check if we sunk the ship or not
        sink = sunkTest(board,letterSpot)
        checkForWin = checkWin(enemy_board)
        if checkForWin  == "win":
            return 3
        elif sink == 1:
            return 2
        return 1

    #Here would be a miss and write a O on that spot
    elif tempBoard[yCoord][xCoord] == "_":
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord] + \
            "O" + tempBoard[yCoord][xCoord+1:]
        print("Shot and a miss!")        
        
        board = open(personal_board, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        return 0
    else:
        print("There has been a shot here already")
        return 350


#only called from 3 var.
def shot_board_write(xCoord,yCoord):
    print("im here")
    #enemy board
    board2 = open(enemy_board, "r")
    tempBoard2 = board2.readlines()
    board2.close()
    #shotboard
    board3 = open(shots_taken, "r")
    tempBoard3 = board3.readlines()
    board3.close()


    print("Attempted to fire here " + str(xCoord) + " " + str(yCoord))
    
    #This spot is a hit on a ship
    if tempBoard2[yCoord][xCoord] != '_' and tempBoard2[yCoord][xCoord] != 'X' and tempBoard2[yCoord][xCoord] != 'O': 
        letterSpot = str(tempBoard2[yCoord][xCoord])
        print("looks like we got a hit!")
        tempBoard3[yCoord] = tempBoard3[yCoord][0:xCoord] + \
            "X" + tempBoard3[yCoord][xCoord+1:]

        board3 = open(shots_taken, "w")
        for i in tempBoard3:
            board3.write(i)
        board3.close()
        # hit = board2.readlines()
        # for i in hit:
        #     if i == 'X' or i == 'O':
        #         board3.write(i) 
        #     else:
        #         board3.write(hit2[i])
        # board3.close()
        # board2.close()

        #When we get a hit we want to check if we sunk the ship or not
        sink = sunkTest(board3,letterSpot)
        checkForWin = checkWin(enemy_board)
        if checkForWin  == "win":
            return 3
        elif sink == 1:
            return 2
        return 1

    #Here would be a miss and write a O on that spot
    elif tempBoard2[yCoord][xCoord] == "_":
        # tempBoard[yCoord] = tempBoard[yCoord][0:xCoord] + \
        #     "O" + tempBoard[yCoord][xCoord+1:]
        print("Shot and a miss!")        
        tempBoard2[yCoord] = tempBoard2[yCoord][0:xCoord] + \
            "O" + tempBoard2[yCoord][xCoord+1:]

        tempBoard3[yCoord] = tempBoard3[yCoord][0:xCoord] + \
            "O" + tempBoard3[yCoord][xCoord+1:]
        # board = open(personal_board, "w")
        # board2 = open(enemy_board, "w")
        board3 = open(shots_taken,"w")

        # for i in tempBoard:
        #     board.write(i)
        # board.close()

        # for i in tempBoard2:
        #     board2.write(i)
        # board2.close()
        for i in tempBoard3:
            board3.write(i)
        board3.close()
        print("woah fuck bud")
        return 0
    else:
        print("There has been a shot here already")
        return 350

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
        personal_string_board = boardWrite(personal_board)
        enemy_string_board = boardWrite(enemy_board)
        shot_string_board = boardWrite(shots_taken)
        self.send_response(200)
        self.end_headers()
        self.send_header('Content-type' , "text/html")
        if self.path == '/own_board.html':
            self.wfile.write(b"<html><h1>Personal Board</h1><style>.grid-container{display: flex;}.grid-item{width: 25px;}</style><body><h1 class = 'container'>"
            +personal_string_board+ b"</h1></body></html>")
        elif self.path == '/opponent_board.html':
            self.wfile.write(b"<html><style>.grid-container{display: flex;}.grid-item{width: 25px;}</style><body><h1 class = 'container'>"
            +enemy_string_board+ b"</h1></body></html>")    
        else:
            self.wfile.write(b"<html><h1>Personal Board</h1><style>.grid-container{display: flex;}.grid-item{width: 25px;}</style><body><h1 class = 'container'>"
            +personal_string_board+ b"</h1></body></html>")
            self.wfile.write(b"<html><h1>Shot Board</h1><style>.grid-container{display: flex;}.grid-item{width: 25px;}</style><body><h1 class = 'container'>"
            +shot_string_board+ b"</h1></body></html>")
        # self.wfile.write(b"<html><h1>Enemy Board</h1><style>.grid-container{display: flex;}.grid-item{width: 25px;}</style><body><h1 class = 'container'>"
        #     +enemy_string_board+ b"</h1></body></html>")

    def do_POST(self): 
        url = 'http://localhost:'+PORT+'?'
        content = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content)            
        post_data = post_data.decode("utf-8")
        print(url + str(post_data))
        coords = re.findall(r'\d+', post_data)
        print(coords)
        x = int(coords[0])
        y = int(coords[1])
        z = int(coords[2])
        if z==1:
            return_message = shot_board_write(x,y)
        else:
            return_message = checkForInput(x,y)
        #For a miss
        if return_message == 0:
            response = BytesIO()
            response.write(b'http://localhost:'+PORT+'?miss=0')
            self.send_response(300)

        #For a hit
        elif return_message == 1:
            print('Help hit')
            response = BytesIO()
            response.write(b'http://localhost:'+PORT+'?hit=1')
            self.send_response(200)

        #For a sink
        elif return_message == 2:
            response = BytesIO()
            aa = str(return_message)
            sink_message = "http://localhost:"+PORT+"?" + aa
            sink_message = sink_message.encode()
            response.write(bytes(sink_message))
            self.send_response(400)
        elif return_message == 3:
            response = BytesIO()
            response.write(b'http://localhost:'+PORT+'?win=3')
            self.send_response(420)
        else:
            response = BytesIO()
            self.send_response(350)

        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        self.wfile.write(response.getvalue())

httpd = HTTPServer(('localhost',int(PORT)), SimpleHTTPRequestHandler)
httpd.serve_forever()


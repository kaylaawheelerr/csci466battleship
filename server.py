from http.server import HTTPServer, BaseHTTPRequestHandler
import re, urllib
from io import BytesIO


#default file paths being used
personal_board = r"/Users/christianmarquardt/Desktop/BattleShip/personal_board.txt"
enemy_board = r"/Users/christianmarquardt/Desktop/BattleShip/enemy_board.txt"


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
            hit = countHit(file,i,j)
            if hit == 'X' or hit =='O':
                numHits +=1
    return numHits


#A simple print board method
def print_board(file):
    board= open(file, "r")
    for i in board:
        print(i)
    board.close()


def checkForInput(xCoord,yCoord):
    if xCoord > 9 or xCoord < 0 and yCoord > 9 or yCoord < 0:
        
    else:
        shotTaken(xCoord,yCoord)

#Here will process the shot
def shotTaken(xCoord,yCoord):
    xCoord = int(xCoord)
    yCoord = int(yCoord)

    board = open(personal_board, "r")
    tempBoard = board.readlines()
    board.close()

    print("Attempted to fire here " + str(xCoord) + " " + str(yCoord))

    #This spot is a hit on a ship
    if tempBoard[yCoord][xCoord] != '_' and tempBoard[yCoord][xCoord] != 'X' and tempBoard[yCoord][xCoord] != 'O':
        print("looks like we got a hit!")
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord]+ "X" + tempBoard[yCoord][xCoord+1:]
        board = open(personal_board, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        print_board(personal_board)

    elif tempBoard[yCoord][xCoord] == "_":
        print("Shot and a miss!")
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord]+ "O" + tempBoard[yCoord][xCoord+1:]
        board = open(personal_board, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        checkForSink(personal_board)
        print_board(personal_board)

def checkForSink(file):
    counterCarrier = 0
    counterBattleShip = 0
    counterCruiser = 0
    counterSubmarine = 0
    counterDestroyer = 0
    sinkList = ""

    board = open(file, "r")
    s = board.readlines()
    board.close()
    print("Sinks so far:")
    for i in range(10):
        for j in range(10):
            if s[i][j] == "C":
                counterCarrier += 1
            elif s[i][j] == "B":
                counterBattleShip += 1
            elif s[i][j] == "R":
                counterCruiser+= 1
            elif s[i][j] == "S":
                counterSubmarine += 1
            elif s[i][j] == "D":
                counterDestroyer += 1
            else:
                pass
    if counterCarrier ==0:
        sinklist = sinkList + "Carrier is sunk \n"
    if counterBattleShip ==0:
        sinklist = sinkList + "Battleship is sunk \n"
    if counterCruiser ==0:
        sinklist = sinkList + "Cruiser is sunk \n"
    if counterSubmarine==0:
        sinklist = sinkList + "Submarine is sunk \n"
    if counterDestroyer ==0:
        sinklist = sinkList + "Destroyer is sunk \n"
    return sinkList

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        boardFile = "Error"
        if(self.path == '/own_board.html'):
                boardFile = print_board('own_board.txt')
        if(self.path == '/opponent_board.html'):
                boardFile = print_board('opponent_board.txt')
        prettyFile = '<html><body><h1><pre>' + boardFile + '</pre></h1></body></html>'
        self.wfile.write(prettyFile.encode())

    def do_POST(self):
        global myBoard
        myBoard = []
        f = open(personal_board, 'r')
        for line in f:
            myBoard.append(list(line))
        f.close()
        coor = urllib.parse.parse_qs(self.path)
        xCoord = int(coor['x'][0])
        yCoord = int(coor['y'][0])
        returnMessage = checkInput(xCoord, yCoord)
        with open(board, 'w') as file:
            for line in myBoard:
                file.write(''.join(line))
        self.send_response(returnMessage[0])
        self.send_header('Content-Type', 'text')
        self.end_headers()
        self.wfile.write(returnMessage[1].encode())
        
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

   
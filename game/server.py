import re
import sys
import urllib
from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


def create_board(board_file):
    f = open(board_file, "r")
    if f.mode == 'r':
        BOARD = (f.read())
        print(BOARD)
    return(BOARD)
        
        
def get_board_string(board):
    board_string =str()
    BOARD = (board.split("\n"))
    for line in BOARD:
        board_string += "<div class = 'grid-container'>"
        for character in line:
            board_string += "<div class = 'grid-item'>" + character + "</div>"
        board_string += "</div>"        
    board_string = str.encode(board_string)
    return(board_string)
    


def handle_play(x, y):
    x= int(x)
    y = int(y)

    # board = open(BOARD, "r")
    # tempBoard = board.readlines()
    # board.close()

    tempBoard = create_board(sys.argv[2])

    print("Attempted to fire here " + str(x) + " " + str(y))

    #This spot is a hit on a ship
    if tempBoard[y-1][x-1] != '_' and tempBoard[y-1][x-1] != 'X' and tempBoard[y-1][x-1] != 'O':
        print("looks like we got a hit!")
        letterSpot = str(tempBoard[y-1][x-1])
        # tempBoard[y-1] = tempBoard[y-1][0:x-1] + \
        #     str("X") + tempBoard[y][x+1:]
        board = open(BOARD, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        #sink = sunkTest(board,letterSpot)
        create_board(BOARD)
        #if sink == "still alive":
            #return 1
        return 1

    elif tempBoard[y][x] == "_":
        print("Shot and a miss!")
        tempBoard[y] = tempBoard[y][0:x] + \
            "O" + tempBoard[y][x+1:]
        board = open(BOARD, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        create_board(BOARD)
        return 0

        
def check_table(hit_spot, x, y):
    if hit_spot == 'D':
        BOARD[x][y] == '.'
    else:
        if BOARD[x][y-1] != BOARD[x][y] and BOARD[x][y+1] != BOARD[x][y]:
            BOARD[x][y] = '.'

BOARD = create_board(sys.argv[2])
PORT = sys.argv[1]
board_string = get_board_string(BOARD)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
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
        x = coords[0]
        y = coords[1]
        result = handle_play(x,y)
        if result == 'miss':
            self.send_response(300)
        elif result == 'taken':
            self.send_response(350)
        else: 
            check_table(BOARD[x][y], x, y)

        

        print("x = " + x, " y = " + y)
        self.send_response(420)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

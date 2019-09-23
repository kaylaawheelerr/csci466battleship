import re
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from io import BytesIO

def create_board(board_file):
    f = open(board_file, "r")
    if f.mode == 'r':
        BOARD = (f.read())
        print(BOARD)
    return(BOARD)
      
def get_board_string(board):
    board_string =str()
    board = board_string.replace("_"," ")
    print(board)
    BOARD = (board.split("\n"))
    i=0
    for line in BOARD:
        board_string += "<div class= inline>"+str(i) + "<div class = 'grid-container'> </div>"
        for character in line:
            board_string += "<div class = 'grid-item'>" + character + "</div>"
        board_string += "</div>"
        i = i+1
        if i ==10:
            board_string = str.encode(board_string)
            return(board_string)
    board_string = str.encode(board_string)
    return(board_string)

def handle_play(x, y):
    selected = oppenentBOARD[x][y].copy()
    if selected == '_':
        shotBOARD[x][y] = 'X'
        return 'miss'
    elif selected == '.':
        return 'taken'
    else:
        return selected
        
def check_table(hit_spot, x, y):
    if hit_spot == 'D':
        BOARD[x][y] == '.'
    else:
        if BOARD[x][y-1] != BOARD[x][y] and BOARD[x][y+1] != BOARD[x][y]:
            BOARD[x][y] = '.'


PORT = int(sys.argv[1])
BOARD = create_board(sys.argv[2])
# shotBOARD = create_shot_board(sys.argv[2])
# oppenentBOARD = get_board_list(create_board(sys.argv[3]))
board_string = get_board_string(BOARD)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.send_header('Content-type' , "text/html")
        self.wfile.write(b"<html><style>.inline{ display:flex}.grid-container{display: flex;}.grid-item{width: 35px; height: 35px; text-align:center; border:solid black 1px}</style><body><h1 class = 'container'>"
        +bytes(board_string)+ 
        b"</h1></body></html>")



    def do_POST(self): 
        # self.end_headers()
        content = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content)

        post_data = post_data.decode("utf-8")
        coords = re.findall(r'\d+', post_data)
        x = coords[0]
        y = coords[1]
        # result = handle_play(x,y)
        # if result == 'miss':
        #     self.send_response(300)
        #     self.end_headers()
        # elif result == 'taken':
        #     self.send_response(350)
        #     self.end_headers()
        # else: 
        #     check_table(BOARD[x][y], x, y)

        

        print("x = " + x, " y = " + y)
        self.send_response_only(420)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
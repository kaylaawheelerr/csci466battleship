import re
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


def create_board(board_file):
    f = open(board_file, "r")
    if f.mode == 'r':
        BOARD = f.read()
        print(BOARD)


def handle_play(x, y):
    selected = BOARD[x][y].copy()
    if selected == '_':
        BOARD[x][y] = '.'
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

BOARD = bytes()
create_board(sys.argv[1])

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


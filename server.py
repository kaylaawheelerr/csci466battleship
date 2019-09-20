from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


#default file paths being used
personal_board = r"/Users/christianmarquardt/Desktop/BattleShip/personal_board.txt"
enemy_board = r"/Users/christianmarquardt/Desktop/BattleShip/enemy_board.txt"

#fillBoard= open(personal_board,"w")
#for i in range(10):
#    fillBoard.write("__________\n")
#fillBoard.close()


def print_board(file):
    board= open(file, "r")
    for i in board:
        print("  ".join(i))
    board.close()

#Here will process the shot
def shotTaken(xCoord,yCoord):
    xCoord = int(xCoord)
    yCoord = int(yCoord)
    print("We are currently trying to fire at " + str(xCoord) + " " + str(yCoord))
    board = open(personal_board, "r")
    print_board(personal_board)
    tempBoard = board.readlines()
    board.close()
    if tempBoard[yCoord][xCoord] !='_' and tempBoard[yCoord][xCoord] != 'X' and tempBoard[yCoord][xCoord] != 'O':
        print("looks like we got a hit!")
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord]+ "X" + tempBoard[yCoord][xCoord+1:]
        board = open(personal_board, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        print_board(personal_board)

    elif tempBoard[yCoord][xCoord] == "_":
        print("Unsuccessful hit")
        tempBoard[yCoord] = tempBoard[yCoord][0:xCoord]+ "O" + tempBoard[yCoord][xCoord+1:]
        board = open(personal_board, "w")

        for i in tempBoard:
            board.write(i)
        board.close()
        print_board(personal_board)

def countHit(file, x, y):
    board = open(file, "r")
    s = board.readlines()
    board.close()
    return s[y][x]

def countBoard(file):
    numHits = 0
    for i in range(10):
        for j in range(10):
            hit = countHit(file,i,j)
            if hit == 'X' or hit =='O':
                numHits +=1
    return numHits

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
    
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

   
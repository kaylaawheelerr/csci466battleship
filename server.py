import socket, re, sys, os


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

def main():
    port= int(sys.argv[1])
    board = sys.argv[2]
    personal_board = board
    print(personal_board)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)

    conn, address = s.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
    #while(countBoard(personal_board) != 17 and countBoard(enemy_board) != 17):
    # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode('utf-8'))  # send data to the client

    conn.close()  # close the connection
   
   
   
   
   
   
   
   


       # s.listen(1)
       ## conn, addr = s.accept()
       # data=conn.recv(153)
    
           # shotTaken(x,y)

main()
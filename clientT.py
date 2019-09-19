
import socket, sys, requests


def client_program():
    IP_Address = str(sys.argv[1])  # as both code is running on same pc
    port = str(sys.argv[2]) # socket server port number
    xCoord = str(sys.argv[3])
    yCoord = str(sys.argv[4])
    http_message = "http://" + IP_Address + ":" + port + "/?x=" + xCoord + "&y=" + yCoord
    print(http_message)
    response = requests.post(http_message) #sends a URL formatted like 'http://0.0.0.0:0000/?x=#&y=#'
    client_socket = socket.socket()  # instantiate
    client_socket.connect((IP_Address, port))  # connect to the server
    http_code = int(response.status_code)
    print(http_code)
    while True:
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
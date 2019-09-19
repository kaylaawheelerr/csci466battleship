import socket


def main():
    ip = "localhost"
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates socket
    s.connect((ip, port))  # connects us to server
    print("Connected")

    #headers
    coordinates = "22"
    conntype = 'Connection: close'
    conttype = 'Content-Type: application/x-uuu-form-urlencoded'
    user = 'User-Agent: client.py'
    contlen = 'Content-Length:  %s' % (len(coordinates))

    s.send(bytes("POST / HTTP/1.1\n%s\n%s\n%s\n%s\n%s" %
                 (conntype, conttype, user, contlen, coordinates)))  # post to server
    data = s.recv(1024)  # decode data we get back from server
    print(data)

    s.close()  # close connection

main()
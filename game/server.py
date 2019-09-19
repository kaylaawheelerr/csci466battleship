import sys
import socket
import requests

def main():

    while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", 8080))
        #print ("Socket binded to port")
        s.listen(1)
        #print ("Socket is listening")
        conn, addr = s.accept()
        print(addr[0])
        data = conn.recv(1024)
        response = 'Thank you'
        if addr[0] == '192.168.1.12':
            print(data)
        else:
            response = "200"

        conntype = 'Connection: close'
        conttype = 'Content-Type: application/x-uuu-form-urlencoded'
        contlen = 'Content-Length:  %s' % (len(response))

        print("\nReceived from client:\n" + data + "\n")

        if response == "404":
            message = ("HTTP/1.1 404\n%s\n%s\n%s" %
                       (conntype, conttype, contlen))
        elif response == "410":
            message = ("HTTP/1.1 410\n%s\n%s\n%s" %
                       (conntype, conttype, contlen))
        elif response == "400":
            message = ("HTTP/1.1 400\n%s\n%s\n%s" %
                       (conntype, conttype, contlen))
        else:
            message = ("HTTP/1.1 200\n%s\n%s\n%s\n%s\n" %
                       (conntype, conttype, contlen, response))

        print("\nSent to client:\n" + message + "\n")
        conn.send(bytes(message))
        s.close()

main()
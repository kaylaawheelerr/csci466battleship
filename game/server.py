#!/usr/bin/env python3

import socket
import urllib.parse

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            data = data.decode('utf-8')
            print(data)
            data = urllib.parse.unquote(data)
            print(data)
            if not data:
                break
            conn.send(bytes('HTTP/1.1 200 OK \
                \nDate: Mon, 27 Jul 2009 12: 28: 53 GMT \
                \nServer: Apache/2.2.14 (Win32) \
                \nLast-Modified: Wed, 22 Jul 2009 19: 15: 56 GMT \
                \nContent-Length: 88 \
                \nContent-Type: text/html \
                \nConnection: Closed', 'utf-8'))

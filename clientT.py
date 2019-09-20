#!/usr/bin/env python3

import socket
import urllib.parse

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8000       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    m = 'POST / localhost:65432 HTTP/1.1\nHost: localhost:65432 \
                    \nContent-Type: application/x-www-form-urlencoded \
                    \nContent-Length: 64\n\nx = 1 & y = 2'
    m = urllib.parse.quote(m)
    m = bytes(m, 'utf-8')
    print("This is ",m)
    s.send(m)
    data = s.recv(1024)

print('Received', repr(data))

# POST / test HTTP/1.1
# Host: foo.example
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 27

# field1 = value1 & field2 = value2

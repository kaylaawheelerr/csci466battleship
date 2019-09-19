import http.server
import socketserver
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    print("serving at port", PORT)

    def do_GET(self):
        if self.path == ("/?x=5&y=10"):
            self.send_response(410)
        else:
	        self.send_response(200)
	        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        print(self.path)




server = socketserver.TCPServer(( ("") , PORT) , Server)
try:
    server.serve_forever()        
except KeyboardInterrupt:
    server.server_close()   

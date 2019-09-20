import http.server
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import re
ip_address = "169.254.126.167"
PORT = 8080
# Handler = http.server.SimpleHTTPRequestHandler
class Server(BaseHTTPRequestHandler):
    print("serving at port", PORT)

    # try:
        # connection, client_address = sock.accept()
        # while True:
    # def do_GET(self):
    #     if self.path == ("/"):
    #         self.wfile.write(bytes("<p>You accessed path: %s </p>"%self.path,"utf-8"))
    #         self.send_response(200)
    #     if self.path == ("/?x=5&y=10"):
    #         self.send_response(410)
    #         self.wfile.write(bytes("<p>You accessed path: %s </p>"%self.path,"utf-8"))
    #         self.responses()
    #         return(10)
    #     else:
    #         self.wfile.write(bytes("<p>You accessed path: %s </p>"%self.path,"utf-8"))
	#         # self.send_response(200)
            # self.send_response(200)
        # print(self.path)

    def do_POST(self):
        self.send_response(202)
        content = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content)
        post_data = post_data.decode("utf-8")
        coords=re.findall(r'\d+',post_data)
        x = coords[0]
        y = coords[1]
        print("x = "+ x, " y = " + y)
        server.close_request
    # finally:
    #     connection.close()

server = socketserver.TCPServer(( ("") , PORT) , Server)
try:
    server.serve_forever()        
except KeyboardInterrupt:
    server.server_close()   

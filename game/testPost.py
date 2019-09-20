# import http.server 
# import http
# import socketserver
# Handler = http.server.SimpleHTTPRequestHandler
# port = 8080
# class S(Handler):
#     def _set_headers(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()

#     def do_GET(self):
#         self._set_headers()
#         self.wfile.write("<html><body><h1>hi!</h1></body></html>")

#     def do_HEAD(self):
#         self._set_headers()
        
#     def do_POST(self):
#         # Doesn't do anything with posted data
#         content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
#         post_data = self.rfile.read(content_length) # <--- Gets the data itself
#         self._set_headers()
#         self.wfile.write("<html><body><h1>POST!</h1></body></html>")
#         print(post_data)
        
# # def run(server_class=http.server, handler_class=S, port=8080):
# #     server_address = ('', port)
# #     httpd = server_class(server_address, handler_class)
# #     print('Starting httpd...')
# # def run()
# with socketserver.TCPServer(("", port), Handler) as httpd:
#     print("serving at port", port)
#     httpd.serve_forever()

# if __name__ == "__main__":
#     from sys import argv

#     # if len(argv) == 2:
#     #     run(port=int(argv[1]))
#     # else:
#     #     run()
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = ""
hostPort = 8080
# HTTPServer.server_bind()
class MyServer(BaseHTTPRequestHandler):

	#	GET is for clients geting the predi
	def do_GET(self):
		self.send_response(200)
		self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))

	#	POST is for submitting data.
	def do_POST(self):

		print("incomming http: " , self.path)

		# content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		# post_data = self.rfile.read(content_length) # <--- Gets the data itself
		self.send_response(200)
		# client.close()

		#import pdb; pdb.set_trace()


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
# print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
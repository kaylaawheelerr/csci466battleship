# load additional Python module
import socket
import http
import requests
import cgi
# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)
# ip_address = 153.90.19.189

# output hostname, domain name and IP address
print ("working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# bind the socket to the port 23456
server_address = (ip_address, 8080)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

# listen for incoming connections (server mode) with one connection at a time
sock.listen(1)
# username="didnt change"
while True:
    print ('waiting for a connection')
    try:
        connection, client_address = sock.accept()
    except KeyboardInterrupt:
        connection.close()
        # show who connected to us
        print ('connection from', client_address)

        # receive the data in small chunks and print it
        while True:
            data = connection.recv(1024)
            # username=''
            if data:
                def do_GET(connection):
                    if connection.path == ("/?x=5&y=10"):
                        connection.send_response(410)
                    else:
    	                connection.send_response(200)

                def do_POST(connection):
                    content = int(connection.headers['Content-Length'])
                    post_data = connection.rfile.read(content)
                    connection.send_response(202)
            else:
                # no more data -- quit the loop
                print ("no more data.")
                break
    finally:
        # Clean up the connection
        # print(username)
        connection.close()
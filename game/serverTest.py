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
                # output received data
                if data == "a":
                    print("the fuck?")
                elif data == "test":
                    print("really??test??")
                print ("Data: %s" % data)
            else:
                # no more data -- quit the loop
                print ("no more data.")
                break
    finally:
        # Clean up the connection
        # print(username)
        connection.close()
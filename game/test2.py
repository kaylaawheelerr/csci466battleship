# load additional Python modules
import socket
import requests
import http
# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)
# ip_address = 153.90.19.189

# bind the socket to the port 23456, and connect
server_address = (ip_address, 8080)
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

data = str(input).encode("utf-8")
sock.sendall

url = 'http://' + ip_address + ':8080' 
myobj = { input : 'Dylan'}

x = requests.post(url, data = myobj)

print(x.text)
# define example data to be sent to the server
# temperature_data = ["15", "22", "21", "26", "25", "19"]
# for entry in temperature_data:
#     print ("data: %s" % entry)
#     new_data = str("temperature: %s\n" % entry).encode("utf-8")
#     sock.sendall(new_data)
    
#     # wait for two seconds
#     time.sleep(2)

# close connection
sock.close()
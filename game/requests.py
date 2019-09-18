import requests
import socket

local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
url = 'http://' + ip_address + ':8080' 
myobj = { input : 'Dylan'}

x = requests.post(url, data = myobj)

print(x.text)
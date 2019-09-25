import requests
import socket
import json
import sys
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
ip = 'http://'+ip_address
url = 'http://localhost:8000' 
myobj = { 'x' : sys.argv[1] , 'y' : sys.argv[2] }
response = (requests.post(url,myobj))
print(response)
if response.status_code == 200:
    print("You got a hit!")
if response.status_code == 300:
    print("Miss! You suck!")
if response.status_code == 350:
    print("Spot already chosen!")
if response.status_code == 400:
    print("You sunk a ship, nice job")
if response.status_code == 420:
    print("You won!")
if response.status_code == 500:
    print("You lost!")

    #TODO make it send a second request to other port
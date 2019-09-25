import requests
import socket
import json
import sys
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
PORT = sys.argv[1] 
url = 'http://localhost:'+ PORT
myobj = { 'x' : sys.argv[2] , 'y' : sys.argv[3]}
response = (requests.post(url,myobj))
print(response)
if response.status_code == 200:
    print("You got a hit!")
    print("HTTP OK")
if response.status_code == 300:
    print("Miss!")
    print("HTTP OK")
if response.status_code == 350:
    print("Spot already chosen!")
    print("HTTP Gone")
if response.status_code == 400:
    print("You sunk a ship, nice job")
    print("HTTP OK")
if response.status_code == 404:
    print("HTTP Not Found")
if response.status_code == 450:
    print("You won!")
    print("HTTP OK")
if response.status_code == 500:
    print("You lost!")

    #TODO make it send a second request to other port
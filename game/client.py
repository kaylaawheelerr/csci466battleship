import requests
import socket
import json
import sys

local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
url = 'http://localhost:8000' 

myobj = { 'x' : sys.argv[1] , 'y' : sys.argv[2] }

response = (requests.post(url,myobj))
print(response.text)
print(response)
if response.status_code == 201:
    print("You got a hit!")
if response.status_code == 300:
    print("Miss! You suck!")
if response.status_code == 208:
    print('You shot off the board')
if response.status_code == 350:
    print("Spot already chosen!")
if response.status_code == 400:
    print("Hit and You sunk a ship!")
if response.status_code == 420:
    print("Hit, Sunk, and You won!")
if response.status_code == 500:
    print("You lost!")

import requests
import socket
import json
import sys
import re

local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
url = 'http://localhost:8000' 

myobj = { 'x' : sys.argv[1] , 'y' : sys.argv[2] }

response = (requests.post(url,myobj))
response_message = response.text
result = re.findall(r'\d+', response_message)
sunk = response_message[-1:]
if sunk != 0 and sunk != 1:
    print(sunk)

# if result[0] == '1':
#     print('hit')
# if result[0] == '0':
#     print('miss')


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


import requests
import socket
import json
import sys
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
url = 'http://localhost:8000' 
# # myobj = { "shot" : "test"}
# url = 'http://httpbin.org/post' 
myobj = { 'x' : sys.argv[1] , 'y' : sys.argv[2] }
# test = { 'path' : "/apply.php"}
# # x = requests.post(url, data = myobj,headers=myobj)
# # x = requests.post(url,data=myobj,headers={'content-type': 'application/json'})
# x = requests.post(url,json.dumps(myobj),headers=myobj)
# y = requests.get(url)
# print(x.text)
# print(x.status_code)
# print(y.form)
# curl -d "foo=bar&bin=go" http://localhost:8080
# requests.get(url,test)
# requests.get(url, myobj)
# print(requests.get(url,myobj))
response = (requests.post(url,myobj))
print(response)
if response.status_code == 200:
    print("You got a hit!")
if response.status_code == 300:
    print("Miss! You suck!")
if response.status_code == 350:
    print("Spot already chosen!")
if response.status_code == 201:
    print("You sunk the Carrier, good work!")
if response.status_code == 202:
    print("You sunk the Battleship, nice work!")
if response.status_code == 203:
    print("You sunk the cRuiser, nice!")
if response.status_code == 204:
    print("You sunk the Submarine!")
if response.status_code == 205:
    print("You sunk the Destroyer!")
if response.status_code == 420:
    print("You won!")
if response.status_code == 500:
    print("You lost!")
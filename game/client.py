import requests
import socket
import json
import sys
import re

local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
url = 'http://localhost:' + sys.argv[1] 
x = sys.argv[2]
y = sys.argv[3]
enemy_board = "opponent_board.txt"
myobj = { 'x' : x , 'y' : y }
response = (requests.post(url,myobj))

shot_board = open(enemy_board, "r")
tempShotBoard = shot_board.readlines()
shot_board.close()

if response.headers.get('hit') == 1:
    tempShotBoard[y] = tempShotBoard[y][0:x] + \
        "X" + tempShotBoard[y][x+1:]
elif response.headers.get('hit') == 0 and response.headers.get('message') == '':
    tempShotBoard[y] = tempShotBoard[y][0:x] + \
        "O" + tempShotBoard[y][x+1:]

shot_board = open(enemy_board, "w")
for i in tempShotBoard:
    print(i)
    shot_board.write(i)
shot_board.close()

if response.status_code == 200:
    if response.headers.get('hit') == 0:
        print('Miss! You Suck!')
    else:
        print('You hit it')
    if response.headers.get('sink') != 0:
        print('You sunk ' + response.headers.get('sink'))
    if response.headers.get('win') == 1:
        print('All ships sunk. You win!')
elif response.status_code == 404:
    print(response.headers.get('message') + ' - You shot off of board!')
elif response.status_code == 409:
    print(response.headers.get('message') + ' - You already shot here!')



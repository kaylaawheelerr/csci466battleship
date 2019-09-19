import http.client
import sys
import urllib.request, urllib.parse, urllib.error
import shutil
import os


############ Fun text formatters
TITLE = "\033[1;34;47m"
IMPORTANT = "\033[1;33;40m"
FAILURE = "\033[1;31;40m"
SUCCESS = "\033[1;32;40m"
DEF_C = "\033[0;37;40m"
ships = {'C': 'Carrier',
            'B': 'Battleship',
            'R': 'Cruiser',
            'S': 'Submarine',
            'D': 'Destroyer',
            }

def printC(color, message):
    print((color + message + DEF_C))


# Invoked when out of bounds coords were sent
def outOfBounds(message):
    printC(IMPORTANT, 'ERROR (Code 404): Coordinates are out of bounds!')

# Invoked when coords were already fired upon
def alreadyFired(message):
    printC(IMPORTANT, 'ERROR (Code 410): Coordinates have already been fired upon! ')

# Invoked when invalid data formatting was used to communicate
def badRequest(message):
    printC(FAILURE, 'ERROR (Code 400): Bad request. Ensure query data is of a proper format. ')

# Invoked when a hit or miss occurred
def processValidResponse(message, xCoord, yCoord):
    parsedResponse = urllib.parse.parse_qs(message)

    # Read in the file
    oboard = []
    f = open('opponent_board.txt', 'r')
    for line in f:
        oboard.append(list(line))

    if(int(parsedResponse['hit'][0]) == 0):
        printC(IMPORTANT, 'You missed!')
        oboard[int(yCoord)][int(xCoord)] = '.'
    if(int(parsedResponse['hit'][0]) == 1):
        printC(SUCCESS, 'You hit!')
        oboard[int(yCoord)][int(xCoord)] = 'X'

    if('sink' in parsedResponse.keys()):
        printC(SUCCESS, 'You sunk a ' + ships[parsedResponse['sink'][0]])

    with open('opponent_board.txt', 'w') as file:
        for line in oboard:
            file.write(''.join(line))


'''
def validateFile():
    ## True if we hava a board
    if(os.path.isfile('opponent_board.txt')):
        return
    else:
        ## True if we have the board template
        if(os.path.isfile('template.txt')):
            shutil.copy('template.txt', 'opponent_board.txt')
        else:
            printC(FAILURE, 'template.txt used to create opponent_board.txt not found!')
'''


# The Setup parses the IP and port and establishes a connection
if __name__ == '__main__':

    if(len(sys.argv) != 5):
        printC(FAILURE, '\nIncorrect number of arguments!')
        print ('Example: python client.py [IP] [PORT] [X coordinate] [Y coordinate] \n')
        sys.exit(1)

    printC(SUCCESS,'\n\n**********Battleship Client**********\n\n')

    # Find the files we need right away, or make them
    #validateFile()


    # Cache off the IP, port, and coordinates for readability's sake
    ip = sys.argv[1]
    port = sys.argv[2]
    xCoord = sys.argv[3]
    yCoord = sys.argv[4]

    headers = {'Content-type':'application/x-www-form-urlencoded'}

    paramList = {'y': yCoord, 'x': xCoord}
    encodedUrl = '/fire&' + urllib.parse.urlencode(paramList)

    print('Attempting to POST to '+ ip + ':' + port)
    conn = http.client.HTTPConnection(host=ip, port=port)
    conn.request("POST", encodedUrl, None, headers)

    response = conn.getresponse()

    if(response.status == 404):
        outOfBounds(response.read())
    elif(response.status == 410):
        alreadyFired(response.read())
    elif(response.status == 400):
        badRequest(response.read())
    else:
        processValidResponse(response.read().decode(), xCoord, yCoord)

    # Close the connection and exit cleanly
    conn.close()
    sys.exit(0)

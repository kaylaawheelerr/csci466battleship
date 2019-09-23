import requests
import socket
import json
import sys
import http.client

local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
port = sys.argv[3]
# connection to hostname on the port.
# s.connect((local_hostname, port))                               
# Receive no more than 1024 bytes
# msg = s.recv(1024)                                     
# s.close()
# print (msg.decode('ascii'))
# conn= http.client.HTTPConnection(local_hostname,8080)

# data = str(input).encode("utf-8")

# # define example data to be sent to the server
# # temperature_data = ["15", "22", "21", "26", "25", "19"]
# # for entry in temperature_data:
# #     print ("data: %s" % entry)
# #     new_data = str("temperature: %s\n" % entry).encode("utf-8")
# #     sock.sendall(new_data)
    
# #     # wait for two seconds
# #     time.sleep(2)

# # close connection
# url = 'http://' + ip_address + ':8000' 
url = 'http://localhost:'+port
headers = {
    'content-type': 'application/json',
}

params = (
    ('priority', 'normal'),
)

data = {
    "x": 3,
    "y": 5
}
# # # myobj = { "shot" : "test"}
# # url = 'http://httpbin.org/post' 
# # x= sys.argv[1]
# # y= sys.argv[2]
# # myobj = { 'x' : 3 , 'y' : 10 }
test = { 'x' : 7 , 'y' : 10}
# conn.request("POST",url,data,headers=headers)

# # # x = requests.post(url, data = myobj,headers=myobj)
# # # x = requests.post(url,data=myobj,headers={'content-type': 'application/json'})
# # x = requests.post(url,json.dumps(myobj),headers=myobj)
# # y = requests.get(url)
# # print(x.text)
# # print(x.status_code)
# # print(y.form)
# # curl -d "foo=bar&bin=go" http://localhost:8080
# # requests.get(url,test)
resp= requests.post(url,test)
# resp = requests.Response
# requests.
print(resp)
# respon=requests.Response
# print(respon)
# sock.sendall
# requests.request("post",url,test)

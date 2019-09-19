import requests
import socket
import json
import sys
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)
url = 'http://' + ip_address + ':8080' 
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
requests.get(url,myobj)
from socket import *
import json

serverName = 'localhost'
serverPort = 12000

username = input('Username: ')
password = input('Password: ')

data = {'username': username, 'password': password}
raw = json.dumps(data)

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(raw.encode())

message = clientSocket.recv(2048)
print(message.decode())

clientSocket.close()
from socket import *
import json

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = input('Type your message: ')
    clientSocket.send(message.encode())
    response = clientSocket.recv(2048)
    print(response.decode())

    if not response: break

clientSocket.close()
from socket import *

serverName = 'localhost'
serverPort = 12000

N = input('N: ')
for i in range(int(N)):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(str(i).encode())
    clientSocket.close()

clientSocket.close()
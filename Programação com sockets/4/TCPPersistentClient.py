from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

N = input('N: ')
for i in range(int(N)):
    clientSocket.send((str(i)).encode())

clientSocket.close()
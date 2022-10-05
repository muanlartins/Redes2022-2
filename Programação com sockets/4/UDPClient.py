from socket import *

serverName = ''
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
N = input('N: ')

for i in range(int(N)):
    clientSocket.sendto(str(i).encode(), (serverName, serverPort))

clientSocket.close()
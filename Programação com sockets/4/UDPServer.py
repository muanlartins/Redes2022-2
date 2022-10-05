from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

while True:
    number, clientAddress = serverSocket.recvfrom(2048)
    print(number.decode())
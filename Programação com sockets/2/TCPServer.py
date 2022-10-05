from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, address = serverSocket.accept()
    print('Connection accepted: ', address)

    while True:
        message = connectionSocket.recv(2048)
        if not message: break

        print('Server received: ', message.decode())
        modifiedMessage = message.decode().upper()
        connectionSocket.send(modifiedMessage.encode())

    print('Connection closed: ', address)
    connectionSocket.close()

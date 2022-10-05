from socket import *
import json

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

logins = [('luan', '123'), ('martins', '321')]

while True:
    connectionSocket, address = serverSocket.accept()
    print('User connected from address: ', address)

    raw = connectionSocket.recv(2048)
    data = json.loads(raw.decode())

    print(data)

    username = data['username']
    password = data['password']

    if ((username, password) in logins): connectionSocket.send('Login successful'.encode())
    else: connectionSocket.send('Wrong username or password'.encode())

    print('Connection closed: ', address)
    connectionSocket.close()

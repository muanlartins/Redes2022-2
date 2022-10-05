from socket import *
from threading import Thread

serverPort = 12000

def server(number):
    print(f'Server of number {number} is ready to receive')
    while True:
        connectionSocket, address = serverSocket.accept()
        print(f'Connection accepted on server number {number}: ', address)

        while True:
            message = connectionSocket.recv(2048)
            if not message: break

            print(f'Server {number} received: ', message.decode())
            modifiedMessage = message.decode().upper()
            connectionSocket.send(modifiedMessage.encode())

        print(f'Connection closed on server number {number}: ', address)
        connectionSocket.close()

if __name__ == "__main__":
    n = int(input('Type the number of threads: '))

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(2)

    threads = []
    for i in range(n):
        thread = Thread(target=server, args=[i])
        thread.start()
        threads += [thread]

    for thread in threads: thread.join()
    
    serverSocket.close()
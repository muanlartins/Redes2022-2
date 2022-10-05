from socket import *
from threading import Thread

serverPort = 12000

def server(number):
    print(f'Server of number {number} is ready to receive')
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(f'Server {number} received: ', message.decode())

        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

if __name__ == "__main__":
    n = int(input('Type the number of threads: '))

    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    threads = []
    for i in range(n):
        thread = Thread(target=server, args=[i])
        thread.start()

    for thread in threads: thread.join()



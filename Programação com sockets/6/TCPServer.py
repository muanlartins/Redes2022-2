from socket import *
import json

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)



while True:
    connectionSocket, address = serverSocket.accept()
    print('User connected from address: ', address)

    message = connectionSocket.recv(2048).decode()
    connectionSocket.send('Olá! Bem vindo! Qual o seu nome?'.encode())

    message = connectionSocket.recv(2048).decode()
    connectionSocket.send(
                f'''Certo, {message}! Como posso te ajudar? Digite o número que corresponde à opção desejada:
                    \n1 - Agendar um horário da monitoria
                    \n2 - Listar as próximas atividades da disciplina
                    \n3 - E-mail do professor
                '''.encode())

    close = False

    message = connectionSocket.recv(2048).decode()
    if message == '1':
        connectionSocket.send(
            f'''Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br
            '''.encode())
    elif message == '2':
        connectionSocket.send(
            f'''Fique atento para as datas das próximas atividades. Confira o que vem por aí!
            \n
            \nP1: 26 de maio de 2022
            \nLista 3: 29 de maio de 2022
            '''.encode())
    elif message == '3':
        connectionSocket.send(
            f'''Quer falar com o professor?
            \n O e-email dele é sadoc@dcc.ufrj.br
            '''.encode())
    else:
        connectionSocket.send(
            f'''Obrigado por utilizar nossos serviços! Até logo!
            '''.encode())
        close = True

    if not close:
        message = connectionSocket.recv(2048).decode()
        connectionSocket.send(
                f'''Obrigado por utilizar nossos serviços! Até logo!
                '''.encode())

    print('Connection closed: ', address)
    connectionSocket.close()

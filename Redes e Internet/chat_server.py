import socket

host = '' # Definimos o host | Quando se trata de uma string vazia, é um nome que se refere a todas as interfaces disponíveis

port = 12345 # Definimos a porta

# Criamos o objeto Socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Onde AF_NET se refere ao protocolo IP e o SOCK_STREAM se refere ao protocolo TCP | SOCK_DGRAM é o protocolo UDP 

s.bind((host, port)) # vinculamos o hostname e a porta

s.listen(1) # Servidor fica esperando por alguem cliente, limitando-se a 5 conexões por vez

while True:
    conexão, endereço = s.accept()
    print('Server conectado por', endereço)
    
    while True:
        data = conexão.recv(1024)
        print("Ele: ", data.decode())
        
        resposta = input("Você: ")

        conexão.send(resposta.encode())

    conexão.close()

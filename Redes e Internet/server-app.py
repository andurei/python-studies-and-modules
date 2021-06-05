
import socket


host = '' # Definimos o host | Quando se trata de uma string vazia, é um nome que se refere a todas as interfaces disponíveis

port = 12345 # Definimos a porta

# Criamos o objeto Socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Onde AF_NET se refere ao protocolo IP e o SOCK_STREAM se refere ao protocolo TCP | SOCK_DGRAM é o protocolo UDP 

s.bind((host, port)) # vinculamos o hostname e a porta

s.listen(5) # Servidor fica esperando por alguem cliente (escutando), limitando-se a 5 conexões por vez

while 1:
    
    conn, addr = s.accept() # Aceita a Conexão

    print('Conectado no endereço', addr)

    while 1:

        data = conn.recv(1024) # Recebe os dados com limitação de bytes

        if not data:
            break
    
        conn.send(b'' + data) # Envia string em formato de bytes

       
    conn.close()



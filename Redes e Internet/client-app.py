import socket

host = socket.gethostname() # Pega o ip do host

port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # isso aqui está no server e no cliente

s.connect((host, port)) # (host, bind) é uma tupla; no server seria s.bind((host, port))

message = [b'  Ismael boi'] # mensagem em formato bytes

for line in message: # para cada elemento da mensagem
    s.send(line)  # enviar um caractere
    data = s.recv(1024) # receber os dados limitados em bytes
    
    print('Recebeu', repr(data))  # printa o dado recebido

s.close() # desconecta o cliente




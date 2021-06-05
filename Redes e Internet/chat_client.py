import socket

host = socket.gethostname() # Pega o ip do Host
port = 12345


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # está no cliente e no server

s.connect((host, port))

while 1:
    msg = input("Você: ")
    s.send(msg.encode()) # Envia a mensagem string, faz o encode para bytes e envia

    data = s.recv(1024) # Recebe uma mensagem em formato de bytes
    
    print('Ele: ', data.decode()) #printa a mensagem decodificada para string (.decode())

s.close()

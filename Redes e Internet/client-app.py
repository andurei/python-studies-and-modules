import socket

host = socket.gethostname()
port = 12345


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

message = [b'  Ismael boi']

for line in message:
    s.send(line) 
    data = s.recv(1024)
    print('Recebeu', repr(data))

s.close()




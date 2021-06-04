import socket

host = socket.gethostname()
port = 12345


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    msg = input("Você: ")
    s.send(msg.encode())

    data = s.recv(1024)
    print('Ele: ', data.decode())

s.close()

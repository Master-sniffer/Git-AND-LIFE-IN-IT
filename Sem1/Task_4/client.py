import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('#here ip', 9090))

#msg = input()
msg = "da"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())

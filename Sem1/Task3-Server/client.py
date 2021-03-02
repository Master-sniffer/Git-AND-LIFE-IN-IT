#!/usr/bin/env python

import socket

sock=socket.connect()
sock.connect(('10.0.3.15', 9090))
sock.send('hello world'.encode())

data=sock.recv(1024)
sock.close()

print (data.decode())

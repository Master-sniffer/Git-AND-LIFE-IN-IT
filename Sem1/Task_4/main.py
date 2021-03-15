# Модифицировать код сервера таким образом, чтобы при подключении нового клиента создавался новый поток и вся работа с клиентом выполнялась в нем.

# Проверить возможность подключения нескольких клиентов к этому серверу одновременно.

import socket
import threading
from time import sleep


class T(threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self, name="t" + n)
        self.n = n

    def run(self):  # fucking bullshit
        print("Процесс", self.n)

    def write(self,conn):
        msg = 'Nibba boi'
        data = conn.recv(1024)
        if not data:
            conn.send(("No data, man").encode())
            print("we are")
            
        else:
            msg += data.decode()
            conn.send(msg.encode())

#OR YOU CAN DO THIS WAY
# lis = []  # Base with users
# sock = socket.socket()
# sock.bind(('', 9090))

while True: # можно поставить таймер

    # YOU CAN DO THIS WAY
    lis = []  # Base with users
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(5)
    conn, addr = sock.accept()
    print(addr[0])
    lis.append(conn)
    print (lis)

    for i in range (len(lis)):
        j=T(f"{i}")
        j.start()
        j.write(lis[i])
        conn.close()



